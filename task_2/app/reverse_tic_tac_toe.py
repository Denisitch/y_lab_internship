from tkinter import *
from random import randint
from tkinter import messagebox

GAME = True
FIELD = []
X_COUNT = 0
GRID_SIZE = 10  # размерность поля 10*10
RULE_IN_ROW = 5  # сколько символов в ряд нужно собрать для проигрыша
X_SYMBOL = "X"
O_SYMBOL = "O"
EMPTY_SYMBOL = " "


def draw_window():
    """
    Rendering the game window with Tkinter
    """
    window = Tk()
    window.title("Обратные крестики-нолики")
    for row in range(GRID_SIZE):
        line = []
        for col in range(GRID_SIZE):
            button = Button(
                window,
                text=" ",
                width=3,
                height=2,
                font=("ComicSans", 15, "bold"),
                background="pale green",
                command=lambda r=row, c=col: click(r, c),
            )
            button.grid(row=row, column=col, sticky="NSWE")
            line.append(button)
        FIELD.append(line)
    new_game_button = Button(
        window,
        text="Начать новую игру",
        width=4,
        height=2,
        font=("ComicSans", 15, "bold"),
        command=new_game,
    )
    new_game_button.grid(row=11, column=3, columnspan=4, sticky="NSWE")
    window.mainloop()


def click(row, col):
    """
    Click handling
    :param row: row coordinate
    :param col: column coordinate
    """
    if GAME and FIELD[row][col]["text"] == EMPTY_SYMBOL:
        FIELD[row][col]["text"] = X_SYMBOL
        global X_COUNT
        X_COUNT += 1
        is_loss(X_SYMBOL, row, col)
        if not GAME:
            FIELD[row][col]["background"] = "red"
            game_over(X_SYMBOL)
        if GAME and X_COUNT < GRID_SIZE * GRID_SIZE / 2 + 1:
            row, col = get_opponent_position()
            is_loss(O_SYMBOL, row, col)
            if not GAME:
                FIELD[row][col]["text"] = O_SYMBOL
                FIELD[row][col]["background"] = "red"
                game_over(O_SYMBOL)
        if X_COUNT == GRID_SIZE * GRID_SIZE / 2 + 1:
            messagebox.showinfo("Игра", "Игра закончилась ничьей")


def check_slice(get_slice):
    """
    A decorator that checks the slice for a losing combination
    :param get_slice: slicing function
    """

    def wrapper(*args, **kwargs):
        cur_slice, symbol, y, x = get_slice(*args, **kwargs)
        count_symbol = 0
        for cur_symbol in cur_slice:
            if cur_symbol == symbol:
                count_symbol += 1
                if count_symbol == RULE_IN_ROW:
                    global GAME
                    GAME = False
            else:
                count_symbol = 0
        return cur_slice, symbol, y, x

    return wrapper


@check_slice
def get_horizontal_slice(symbol, y, x):
    """
    Get a list of horizontal values
    :param symbol: "X" or "O"
    :param y: row coordinate
    :param x: column coordinate
    :return: h_slice, symbol, y, x
    """
    h_slice = []
    for x_cur in range(GRID_SIZE):
        h_slice.append(FIELD[y][x_cur]["text"])
    return h_slice, symbol, y, x


@check_slice
def get_vertical_slice(symbol, y, x):
    """
    Get a list of vertical values
    :param symbol: "X" or "O"
    :param y: row coordinate
    :param x: column coordinate
    :return: v_slice, symbol, y, x
    """
    v_slice = []
    for y_cur in range(GRID_SIZE):
        v_slice.append(FIELD[y_cur][x]["text"])
    return v_slice, symbol, y, x


@check_slice
def get_upper_diagonal_slice(symbol, y, x):
    """
    Get a list of values on upper diagonal
    :param symbol: "X" or "O"
    :param y: row coordinate
    :param x: column coordinate
    :return: d_slice, symbol, y, x
    """
    d_slice = []
    min_index = min(x, y)
    cur_y, cur_x = y - min_index, x - min_index
    while True:
        d_slice.append(FIELD[cur_y][cur_x]["text"])
        if cur_y >= GRID_SIZE - 1 or cur_x >= GRID_SIZE - 1:
            break
        cur_y += 1
        cur_x += 1
    return d_slice, symbol, y, x


@check_slice
def get_lower_diagonal_slice(symbol, y, x):
    """
    Get a list of values on lower diagonal
    :param symbol: "X" or "O"
    :param y: row coordinate
    :param x: column coordinate
    :return: d_slice, symbol, y, x
    """
    d_slice = []
    min_index = min(GRID_SIZE - 1 - y, x)
    cur_y, cur_x = y + min_index, x - min_index
    while True:
        d_slice.append(FIELD[cur_y][cur_x]["text"])
        if cur_y <= 0 or cur_x >= GRID_SIZE - 1:
            break
        cur_y -= 1
        cur_x += 1
    return d_slice, symbol, y, x


def is_loss(symbol, y, x):
    """
    Conditions of loss
    :param symbol:
    :param y: row coordinate
    :param x: column coordinate
    """
    get_horizontal_slice(symbol, y, x)
    get_vertical_slice(symbol, y, x)
    get_upper_diagonal_slice(symbol, y, x)
    get_lower_diagonal_slice(symbol, y, x)


def new_game():
    """
    A button that clears the field and starts the game again
    """
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            FIELD[row][col]["text"] = EMPTY_SYMBOL
            FIELD[row][col]["background"] = "pale green"
    global GAME
    GAME = True
    global X_COUNT
    X_COUNT = 0


def game_over(symbol):
    """
    Ending the game and showing the winner window
    :param symbol: "X" or "O"
    """
    if symbol == X_SYMBOL:
        messagebox.showinfo("Проигрыш!", "Ты проиграл!")
    else:
        messagebox.showinfo("Победа!", "Ты выиграл!")


def get_opponent_position():
    """
    Recording opponent turn
    :return: row and column coordinate
    """
    count_loop = 0
    while count_loop < GRID_SIZE * GRID_SIZE:
        global GAME
        GAME = True
        y, x = randint(0, GRID_SIZE - 1), randint(0, GRID_SIZE - 1)
        while FIELD[y][x]["text"] != EMPTY_SYMBOL:
            x, y = randint(0, GRID_SIZE - 1), randint(0, GRID_SIZE - 1)
            continue
        board = [FIELD[y].copy() for y in range(GRID_SIZE)]
        board[y][x]["text"] = O_SYMBOL
        is_loss(O_SYMBOL, y, x)
        if GAME:
            return y, x
        else:
            count_loop += 1
            board[y][x]["text"] = EMPTY_SYMBOL
            continue
    return y, x
