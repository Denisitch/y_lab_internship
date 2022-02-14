"""The module contains the calculator interface function."""

from math import pi
import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Combobox
from typing import Tuple, NoReturn, Any, List
import matplotlib.pyplot as plt
import numpy as np

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

    if volume_box.get() == "Сфера":
        label_1["text"] = "Введите радиус r"

        entry_1.pack(side="left", anchor="nw", padx=14, pady=20)

    if volume_box.get() == "Конус":
        label_1["text"] = "Введите радиус r"
        label_2["text"] = "Введите высоту h"

        entry_1.pack(side="left", anchor="nw", padx=14, pady=20)
        entry_2.pack(side="left", anchor="nw", padx=11, pady=20)

    if volume_box.get() == "Цилиндр":
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
            calc_label_1["text"] = f"Площадь круга: {circle.area()}"
            calc_label_2["text"] = f"Периметр круга: {circle.perimeter()}"

            plot_circle = plt.Circle((0, 0), r, color="green", fill=False)
            ax: Any = plt.gca()
            ax.cla()
            ax.set_xlim((-r, r))
            ax.set_ylim((-r, r))
            ax.add_patch(plot_circle)
        except ValueError:
            messagebox.showinfo("Ошибка!", "Введите положительное число!")
            return

    if flat_box.get() == "Квадрат":
        try:
            a: float = float(entry_data_1)
            square: Square = Square(a)
            calc_label_1["text"] = f"Площадь квадрата: {square.area()}"
            calc_label_2["text"] = f"Периметр квадрата: {square.perimeter()}"

            plot_square = plt.Rectangle((0, 0), a, a, color="green", fill=False)
            ax: Any = plt.gca()
            ax.cla()
            ax.set_xlim((0, a))
            ax.set_ylim((0, a))
            ax.add_patch(plot_square)
        except ValueError:
            messagebox.showinfo("Ошибка!", "Введите положительное число!")
            return

    if flat_box.get() == "Прямоугольник":
        try:
            a: float = float(entry_data_1)
            b: float = float(entry_data_2)
            rectangle: Rectangle = Rectangle(a, b)
            calc_label_1["text"] = f"Площадь прямоугольника: {rectangle.area()}"
            calc_label_2["text"] = f"Периметр прямоугольника: {rectangle.perimeter()}"

            plot_rectangle = plt.Rectangle((0, 0), a, b, color="green", fill=False)
            ax: Any = plt.gca()
            ax.cla()
            ax.set_xlim((-20, 20))
            ax.set_ylim((-20, 20))
            ax.add_patch(plot_rectangle)
        except ValueError:
            messagebox.showinfo("Ошибка!", "Введите положительное число!")
            return

    if flat_box.get() == "Треугольник":
        try:
            a: float = float(entry_data_1)
            b: float = float(entry_data_2)
            c: float = float(entry_data_3)
            triangle: Triangle = Triangle(a, b, c)
            calc_label_1["text"] = f"Площадь треугольника: {triangle.area()}"
            calc_label_2["text"] = f"Периметр треугольника: {triangle.perimeter()}"

            x: float = (a**2 + b**2 - c**2) / (2 * a)
            y: float = (b**2 - x**2) ** (1 / 2)

            points: Tuple[List[float, float], ...] = ([0, 0], [a, 0], [x, y])
            plot_triangle = plt.Polygon(points, color="green", fill=False)
            ax: Any = plt.gca()
            ax.cla()
            ax.set_xlim((-20, 20))
            ax.set_ylim((-20, 20))
            ax.add_patch(plot_triangle)
        except ValueError:
            messagebox.showinfo("Ошибка!", "Введите положительное число!")
            return

    if flat_box.get() == "Трапеция":
        try:
            a: float = float(entry_data_1)
            b: float = float(entry_data_2)
            h: float = float(entry_data_3)
            trapezoid: Trapezoid = Trapezoid(a, b, h)
            calc_label_1["text"] = f"Площадь трапеции: {trapezoid.area()}"
            calc_label_2["text"] = f"Средняя линия: {trapezoid.middle_line()}"

            points: Tuple[List[float, float], ...] = (
                [0, 0],
                [a, 0],
                [a / 2 + b / 2, h],
                [a / 2 - b / 2, h],
            )
            plot_trapezoid = plt.Polygon(points, color="green", fill=False)
            ax: Any = plt.gca()
            ax.cla()
            ax.set_xlim((-20, 20))
            ax.set_ylim((-20, 20))
            ax.add_patch(plot_trapezoid)
        except ValueError:
            messagebox.showinfo("Ошибка!", "Введите положительное число!")
            return

    if flat_box.get() == "Ромб":
        try:
            a: float = float(entry_data_1)
            h: float = float(entry_data_2)
            rhombus: Rhombus = Rhombus(a, h)
            calc_label_1["text"] = f"Площадь ромба: {rhombus.area()}"
            calc_label_2["text"] = f"Периметр ромба: {rhombus.perimeter()}"

            points: Tuple[List[float, float], ...] = (
                [0, 0],
                [a, 0],
                [a + (a**2 - h**2) ** (1 / 2), h],
                [(a**2 - h**2) ** (1 / 2), h],
            )
            plot_rhombus = plt.Polygon(points, color="green", fill=False)
            ax: Any = plt.gca()
            ax.cla()
            ax.set_xlim((-20, 20))
            ax.set_ylim((-20, 20))
            ax.add_patch(plot_rhombus)
        except ValueError:
            messagebox.showinfo("Ошибка!", "Введите положительное число!")
            return

    if volume_box.get() == "Сфера":
        try:
            r: float = float(entry_data_1)
            sphere: Sphere = Sphere(r)
            calc_label_1["text"] = f"Площадь сферы: {sphere.area()}"
            calc_label_2["text"] = f"Объем сферы: {sphere.volume()}"

            u: Any = np.linspace(0, 2 * pi, 100)
            v: Any = np.linspace(0, pi, 100)

            x: float = r * np.outer(np.cos(u), np.sin(v))
            y: float = r * np.outer(np.sin(u), np.sin(v))
            z: float = r * np.outer(np.ones(np.size(u)), np.cos(v))

            fig = plt.figure()
            ax = fig.add_subplot(111, projection="3d")
            ax.plot_surface(x, y, z, color="green")
        except ValueError:
            messagebox.showinfo("Ошибка!", "Введите положительное число!")
            return

    if volume_box.get() == "Куб":
        try:
            a: int = int(entry_data_1)
            cube: Cube = Cube(a)
            calc_label_1["text"] = f"Площадь куба: {cube.area()}"
            calc_label_2["text"] = f"Объем куба: {cube.volume()}"

            axes: List[int] = [a, a, a]
            data: Any = np.ones(axes, dtype=np.bool)
            fig: Any = plt.figure()
            ax: Any = fig.add_subplot(111, projection="3d")
            ax.voxels(data, facecolors="green")
        except ValueError:
            messagebox.showinfo("Ошибка!", "Введите положительное число!")
            return

    if volume_box.get() == "Параллелепипед":
        try:
            a: int = int(entry_data_1)
            b: int = int(entry_data_2)
            c: int = int(entry_data_3)
            parallelepiped: Parallelepiped = Parallelepiped(a, b, c)
            calc_label_1["text"] = f"Площадь параллелепипеда: {parallelepiped.area()}"
            calc_label_2["text"] = f"Объем параллелепипеда: {parallelepiped.volume()}"

            axes: List[int] = [a, b, c]
            data: Any = np.ones(axes, dtype=np.bool)
            fig: Any = plt.figure()
            ax: Any = fig.add_subplot(111, projection="3d")
            ax.voxels(data, facecolors="green")
        except ValueError:
            messagebox.showinfo("Ошибка!", "Введите положительное число!")
            return

    if volume_box.get() == "Пирамида":
        try:
            a: float = float(entry_data_1)
            h: float = float(entry_data_2)
            n: int = int(entry_data_3)
            pyramid: Pyramid = Pyramid(a, h, n)
            calc_label_1["text"] = f"Площадь пирамиды: {pyramid.area()}"
            calc_label_2["text"] = f"Объем пирамиды: {pyramid.volume()}"

            r: float = a / (2 * np.sin(pi / n))
            X: List[float] = []
            Y: List[float] = []
            Z: Any = np.zeros(n + 1)
            Z[n] = h

            for i in range(0, n):
                x: float = r * np.cos((2 * pi * i) / n)
                y: float = r * np.sin((2 * pi * i) / n)
                X.append(x)
                Y.append(y)

            X.append(0)
            Y.append(0)
            fig: Any = plt.figure()
            ax: Any = fig.add_subplot(111, projection="3d")
            ax.plot_trisurf(X, Y, Z, color="green")
        except ValueError:
            messagebox.showinfo("Ошибка!", "Введите положительное число!")
            return

    if volume_box.get() == "Цилиндр":
        try:
            r: float = float(entry_data_1)
            h: float = float(entry_data_2)
            cylinder: Cylinder = Cylinder(r, h)
            calc_label_1["text"] = f"Площадь цилиндра: {cylinder.area()}"
            calc_label_2["text"] = f"Объем цилиндра: {cylinder.volume()}"

            u: Any = np.linspace(0, 2 * pi, 50)
            height: Any = np.linspace(0, h, 20)

            x: float = r * np.outer(np.sin(u), np.ones(np.size(height)))
            y: float = r * np.outer(np.cos(u), np.ones(np.size(height)))
            z: float = np.outer(np.ones(np.size(u)), height)

            fig: Any = plt.figure()
            ax: Any = fig.add_subplot(111, projection="3d")
            ax.plot_surface(x, y, z, color="green")
        except ValueError:
            messagebox.showinfo("Ошибка!", "Введите положительное число!")
            return

    if volume_box.get() == "Конус":
        try:
            r: float = float(entry_data_1)
            h: float = float(entry_data_2)
            cone: Cone = Cone(r, h)
            calc_label_1["text"] = f"Площадь конуса: {cone.area()}"
            calc_label_2["text"] = f"Объем конуса: {cone.volume()}"

            theta: Any = np.linspace(0, 2 * pi, 90)
            radius: Any = np.linspace(0, r, 50)
            T, R = np.meshgrid(theta, radius)

            x: float = R * np.cos(T)
            y: float = R * np.sin(T)
            z: float = np.sqrt(x**2 + y**2) * (h / r)

            fig: Any = plt.figure()
            ax: Any = fig.add_subplot(111, projection="3d")
            ax.plot_surface(x, y, z, color="green")

            ax.invert_zaxis()
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
