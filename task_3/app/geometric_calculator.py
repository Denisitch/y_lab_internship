"""The module contains the calculator interface function."""
import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Combobox
from typing import NoReturn
import matplotlib.pyplot as plt

from task_3.app.figure import (
    Circle,
    Square,
    Rectangle,
    Triangle,
    Trapezoid,
    Rhombus,
    Sphere,
    Cube,
    Parallelepiped,
    Pyramid,
    Cylinder,
    Cone,
)

from task_3.app.renderer_figures import RendererFlatFigures, RendererVolumeFigures


def flat_click(case) -> NoReturn:
    """
    Handler for selecting an element from the first dropdown list (flat figures).
    """
    volume_box.set("")

    label_2["text"] = ""
    label_3["text"] = ""

    calc_label_1["text"] = ""
    calc_label_2["text"] = ""
    calc_label_3["text"] = ""

    calculate_btn.pack(side="left", anchor="nw", padx=30)

    entry_2.pack_forget()
    entry_3.pack_forget()
    draw_btn.pack_forget()

    if flat_box.get() == "Круг":
        label_1["text"] = "Введите радиус r"
        entry_1.pack(side="left", anchor="nw", padx=15, pady=18)

    if flat_box.get() == "Квадрат":
        label_1["text"] = "Введите сторону a"
        entry_1.pack(side="left", anchor="nw", padx=15, pady=18)

    if flat_box.get() == "Прямоугольник":
        label_1["text"] = "Введите сторону a"
        label_2["text"] = "Введите сторону b"

        entry_1.pack(side="left", anchor="nw", padx=15, pady=18)
        entry_2.pack(side="left", anchor="nw", padx=15, pady=18)

    if flat_box.get() == "Треугольник":
        label_1["text"] = "Введите сторону a"
        label_2["text"] = "Введите сторону b"
        label_3["text"] = "Введите сторону c"

        entry_1.pack(side="left", anchor="nw", padx=15, pady=18)
        entry_2.pack(side="left", anchor="nw", padx=15, pady=18)
        entry_3.pack(side="left", anchor="nw", padx=15, pady=18)

    if flat_box.get() == "Трапеция":
        label_1["text"] = "Введите сторону a"
        label_2["text"] = "Введите сторону b"
        label_3["text"] = "Введите высоту h"

        entry_1.pack(side="left", anchor="nw", padx=15, pady=18)
        entry_2.pack(side="left", anchor="nw", padx=15, pady=18)
        entry_3.pack(side="left", anchor="nw", padx=15, pady=18)

    if flat_box.get() == "Ромб":
        label_1["text"] = "Введите сторону a"
        label_2["text"] = "Введите высоту h"

        entry_1.pack(side="left", anchor="nw", padx=15, pady=18)
        entry_2.pack(side="left", anchor="nw", padx=15, pady=18)


def volume_click(case) -> NoReturn:
    """
    Handler for selecting an element from the second dropdown list (volume figures).
    """
    flat_box.set("")

    calculate_btn.pack(side="left", anchor="nw", padx=30)

    label_2["text"] = ""
    label_3["text"] = ""
    calc_label_1["text"] = ""
    calc_label_2["text"] = ""
    calc_label_3["text"] = ""

    entry_2.pack_forget()
    entry_3.pack_forget()
    draw_btn.pack_forget()

    if volume_box.get() == "Сфера":
        label_1["text"] = "Введите радиус r"

        entry_1.pack(side="left", anchor="nw", padx=14, pady=20)

    if volume_box.get() == "Куб":
        label_1["text"] = "Введите сторону a"

        entry_1.pack(side="left", anchor="nw", padx=14, pady=20)

    if volume_box.get() == "Параллелепипед":
        label_1["text"] = "Введите сторону a"
        label_2["text"] = "Введите сторону b"
        label_3["text"] = "Введите сторону c"

        entry_1.pack(side="left", anchor="nw", padx=14, pady=20)
        entry_2.pack(side="left", anchor="nw", padx=14, pady=20)
        entry_3.pack(side="left", anchor="nw", padx=14, pady=20)

    if volume_box.get() == "Пирамида":
        label_1["text"] = "Введите сторону a"
        label_2["text"] = "Количество сторон n"
        label_3["text"] = "Введите высоту h"

        entry_1.pack(side="left", anchor="nw", padx=14, pady=20)
        entry_2.pack(side="left", anchor="nw", padx=0, pady=20)
        entry_3.pack(side="left", anchor="nw", padx=20, pady=20)

    if volume_box.get() == "Цилиндр":
        label_1["text"] = "Введите радиус r"
        label_2["text"] = "Введите высоту h"

        entry_1.pack(side="left", anchor="nw", padx=14, pady=20)
        entry_2.pack(side="left", anchor="nw", padx=11, pady=20)

    if volume_box.get() == "Конус":
        label_1["text"] = "Введите радиус r"
        label_2["text"] = "Введите высоту h"

        entry_1.pack(side="left", anchor="nw", padx=14, pady=20)
        entry_2.pack(side="left", anchor="nw", padx=11, pady=20)


def click() -> NoReturn:
    """
    User input handler.
    """
    entry_data_1 = entry_1.get()
    entry_data_2 = entry_2.get()
    entry_data_3 = entry_3.get()
    draw_btn.pack(side="left", anchor="nw", padx=30)

    if flat_box.get() == "Круг":
        try:
            r: float = float(entry_data_1)

            circle: Circle = Circle(r)
            calc_label_1["text"] = f"Площадь круга: {circle.area}"
            calc_label_2["text"] = f"Периметр круга: {circle.perimeter}"

            RendererFlatFigures.get_plot_circle(r)

        except ValueError:
            messagebox.showinfo("Ошибка!", "Введите положительное число!")
            return

    if flat_box.get() == "Квадрат":
        try:
            a: float = float(entry_data_1)
            square: Square = Square(a)
            calc_label_1["text"] = f"Площадь квадрата: {square.area}"
            calc_label_2["text"] = f"Периметр квадрата: {square.perimeter}"

            RendererFlatFigures.get_plot_square(a)

        except ValueError:
            messagebox.showinfo("Ошибка!", "Введите положительное число!")
            return

    if flat_box.get() == "Прямоугольник":
        try:
            a: float = float(entry_data_1)
            b: float = float(entry_data_2)
            rectangle: Rectangle = Rectangle(a, b)
            calc_label_1["text"] = f"Площадь прямоугольника: {rectangle.area}"
            calc_label_2["text"] = f"Периметр прямоугольника: {rectangle.perimeter}"

            RendererFlatFigures.get_plot_rectangle(a, b)

        except ValueError:
            messagebox.showinfo("Ошибка!", "Введите положительное число!")
            return

    if flat_box.get() == "Треугольник":
        try:
            a: float = float(entry_data_1)
            b: float = float(entry_data_2)
            c: float = float(entry_data_3)
            triangle: Triangle = Triangle(a, b, c)
            calc_label_1["text"] = f"Площадь треугольника: {triangle.area}"
            calc_label_2["text"] = f"Периметр треугольника: {triangle.perimeter}"

            RendererFlatFigures.get_plot_triangle(a, b, c)

        except ValueError:
            messagebox.showinfo("Ошибка!", "Введите положительное число!")
            return
        except AttributeError:
            messagebox.showinfo("Ошибка!", "Такой треугольник не существует!")
            return

    if flat_box.get() == "Трапеция":
        try:
            a: float = float(entry_data_1)
            b: float = float(entry_data_2)
            h: float = float(entry_data_3)
            trapezoid: Trapezoid = Trapezoid(a, b, h)
            calc_label_1["text"] = f"Площадь трапеции: {trapezoid.area}"
            calc_label_2["text"] = f"Средняя линия: {trapezoid.middle_line}"

            RendererFlatFigures.get_plot_trapezoid(a, b, h)

        except ValueError:
            messagebox.showinfo("Ошибка!", "Введите положительное число!")
            return

    if flat_box.get() == "Ромб":
        try:
            a: float = float(entry_data_1)
            h: float = float(entry_data_2)
            rhombus: Rhombus = Rhombus(a, h)
            calc_label_1["text"] = f"Площадь ромба: {rhombus.area}"
            calc_label_2["text"] = f"Периметр ромба: {rhombus.perimeter}"

            RendererFlatFigures.get_plot_rhombus(a, h)

        except ValueError:
            messagebox.showinfo("Ошибка!", "Введите положительное число!")
            return

    if volume_box.get() == "Сфера":
        try:
            r: float = float(entry_data_1)
            sphere: Sphere = Sphere(r)
            calc_label_1["text"] = f"Площадь сферы: {sphere.area}"
            calc_label_2["text"] = f"Объем сферы: {sphere.volume}"

            RendererVolumeFigures.get_plot_sphere(r)

        except ValueError:
            messagebox.showinfo("Ошибка!", "Введите положительное число!")
            return

    if volume_box.get() == "Куб":
        try:
            a: int = int(entry_data_1)
            cube: Cube = Cube(a)
            calc_label_1["text"] = f"Площадь куба: {cube.area}"
            calc_label_2["text"] = f"Объем куба: {cube.volume}"

            RendererVolumeFigures.get_plot_cube(a)

        except ValueError:
            messagebox.showinfo("Ошибка!", "Введите положительное число!")
            return

    if volume_box.get() == "Параллелепипед":
        try:
            a: int = int(entry_data_1)
            b: int = int(entry_data_2)
            c: int = int(entry_data_3)
            parallelepiped: Parallelepiped = Parallelepiped(a, b, c)
            calc_label_1["text"] = f"Площадь параллелепипеда: {parallelepiped.area}"
            calc_label_2["text"] = f"Объем параллелепипеда: {parallelepiped.volume}"

            RendererVolumeFigures.get_plot_parallelepiped(a, b, c)

        except ValueError:
            messagebox.showinfo("Ошибка!", "Введите положительное число!")
            return

    if volume_box.get() == "Пирамида":
        try:
            a: float = float(entry_data_1)
            h: float = float(entry_data_2)
            n: int = int(entry_data_3)
            pyramid: Pyramid = Pyramid(a, h, n)
            calc_label_1["text"] = f"Площадь пирамиды: {pyramid.area}"
            calc_label_2["text"] = f"Объем пирамиды: {pyramid.volume}"

            RendererVolumeFigures.get_plot_pyramid(a, h, n)

        except ValueError:
            messagebox.showinfo("Ошибка!", "Введите положительное число!")
            return

    if volume_box.get() == "Цилиндр":
        try:
            r: float = float(entry_data_1)
            h: float = float(entry_data_2)
            cylinder: Cylinder = Cylinder(r, h)
            calc_label_1["text"] = f"Площадь цилиндра: {cylinder.area}"
            calc_label_2["text"] = f"Объем цилиндра: {cylinder.volume}"

            RendererVolumeFigures.get_plot_cylinder(r, h)

        except ValueError:
            messagebox.showinfo("Ошибка!", "Введите положительное число!")
            return

    if volume_box.get() == "Конус":
        try:
            r: float = float(entry_data_1)
            h: float = float(entry_data_2)
            cone: Cone = Cone(r, h)
            calc_label_1["text"] = f"Площадь конуса: {cone.area}"
            calc_label_2["text"] = f"Объем конуса: {cone.volume}"

            RendererVolumeFigures.get_plot_cone(r, h)

        except ValueError:
            messagebox.showinfo("Ошибка!", "Введите положительное число!")
            return


window = tk.Tk()
window.title("Геометрический калькулятор")
window.geometry("550x550")

frame_1 = tk.Frame(window)
frame_2 = tk.Frame(window)
frame_3 = tk.Frame(window)

header_1 = tk.Label(text="Выберите фигуру", font=("ComicSans", 14, "bold"), height=2)
header_2 = tk.Label(text="Плоские фигуры", font=("ComicSans", 14), height=2)
header_3 = tk.Label(text="Объемные фигуры", font=("ComicSans", 14), height=2)

header_1.pack()
header_2.pack(side="top", anchor="nw", padx=30)

flat_box = Combobox(window, font="ComicSans")
flat_box["values"] = (
    Circle.title,
    Square.title,
    Rectangle.title,
    Triangle.title,
    Trapezoid.title,
    Rhombus.title,
)
flat_box.bind("<<ComboboxSelected>>", flat_click)
flat_box.pack(side="top", anchor="nw", padx=30)

header_3.pack(side="top", anchor="nw", padx=30)

volume_box = Combobox(window, font="ComicSans")
volume_box["values"] = (
    Cube.title,
    Parallelepiped.title,
    Pyramid.title,
    Sphere.title,
    Cone.title,
    Cylinder.title,
)
volume_box.bind("<<ComboboxSelected>>", volume_click)
volume_box.pack(side="top", anchor="nw", padx=34)

label_1 = tk.Label(frame_1, text="", font=("ComicSans", 14), justify="left")
entry_1 = tk.Entry(frame_1, width="18")

label_2 = tk.Label(frame_2, text="", font=("ComicSans", 14), justify="left")
entry_2 = tk.Entry(frame_2, width="18")

label_3 = tk.Label(frame_3, text="", font=("ComicSans", 14), justify="left")
entry_3 = tk.Entry(frame_3, width="18")

calc_label_1 = tk.Label(text="", font=("ComicSans", 14), justify="left")
calc_label_2 = tk.Label(text="", font=("ComicSans", 14), justify="left")
calc_label_3 = tk.Label(text="", font=("ComicSans", 14), justify="left")

label_1.pack(side="left", anchor="nw", padx=30, pady=18)
label_2.pack(side="left", anchor="nw", padx=30, pady=18)
label_3.pack(side="left", anchor="nw", padx=30, pady=18)

frame_1.pack(side="top", anchor="nw")
frame_2.pack(side="top", anchor="nw")
frame_3.pack(side="top", anchor="nw")

calculate_btn = tk.Button(text="Вычислить", command=lambda: click())
draw_btn = tk.Button(text="Построить фигуру", command=lambda: plt.show())

calc_label_1.pack(side="top", anchor="nw", padx=30)
calc_label_2.pack(side="top", anchor="nw", padx=30)
