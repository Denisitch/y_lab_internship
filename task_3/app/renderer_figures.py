"""The module contains logic for drawing shapes."""
import math
from typing import Tuple, Any, List
import matplotlib.pyplot as plt
import numpy as np


class RendererFlatFigures:

    @staticmethod
    def get_plot_circle(r):
        """
        Renderer a circle
        :param float r: radius of the circle
        """
        ax: Any = plt.gca()
        ax.set_aspect('equal')
        theta = np.linspace(0, 2 * np.pi, 100)
        ax.plot(r * np.cos(theta), r * np.sin(theta), color='green')
        plot_circle = plt.Circle((0, 0), r, color="green", fill=False)
        ax.add_patch(plot_circle)

    @staticmethod
    def get_plot_square(a):
        """
        Renderer a square
        :param float a: side length of the square
        """
        ax: Any = plt.gca()
        ax.set_aspect('equal')
        point = np.array([[0, 0], [a, 0], [a, a], [0, a], [0, 0]])
        ax.plot(point[:, 0], point[:, 1], '-')
        plot_square = plt.Rectangle((0, 0), a, a, color="green", fill=False)
        ax.add_patch(plot_square)

    @staticmethod
    def get_plot_rectangle(a, b):
        """
        Renderer a rectangle
        :param float a: side length of the rectangle
        :param float b: side length of the rectangle
        """
        ax: Any = plt.gca()
        ax.set_aspect('equal')
        point = np.array([[0, 0], [a, 0], [a, b], [0, b], [0, 0]])
        ax.plot(point[:, 0], point[:, 1], '-')
        plot_rectangle = plt.Rectangle((0, 0), a, b, color="green", fill=False)
        ax.add_patch(plot_rectangle)

    @staticmethod
    def get_plot_triangle(a, b, c):
        """
        Renderer a triangle
        :param float a: side length of the triangle
        :param float b: side length of the triangle
        :param float c: side length of the triangle
        """
        alpha = math.asin((a ** 2 + b ** 2 - c ** 2) / (2 * a * b))
        x, y = b * math.sin(alpha), b * math.cos(alpha)
        ax: Any = plt.gca()
        ax.set_aspect('equal')
        point = np.array([[0, 0], [a, 0], [x, y], [0, 0]])
        ax.plot(point[:, 0], point[:, 1], '-')
        plot_triangle = plt.Polygon(point, color="green", fill=False)
        ax.add_patch(plot_triangle)

    @staticmethod
    def get_plot_trapezoid(a, b, h):
        """
        Renderer a trapeze
        :param float a: side length of the trapeze
        :param float b: side length of the trapeze
        :param float h: length of the height of trapeze
        """
        points: Tuple[List[float, float], ...] = (
            [0, 0],
            [a, 0],
            [a / 2 + b / 2, h],
            [a / 2 - b / 2, h],
        )
        ax: Any = plt.gca()
        ax.set_aspect('equal')
        # ax.plot(points[:, 0], points[:, 1], '-')
        plot_trapezoid = plt.Polygon(points, color="green", fill=False)
        ax.add_patch(plot_trapezoid)

    @staticmethod
    def get_plot_rhombus(a, h):
        """
        Renderer a rhombus
        :param float a: side length of the rhombus
        :param float h: length of the height of rhombus
        """
        points: Tuple[List[float, float], ...] = (
            [0, 0],
            [a, 0],
            [a + (a ** 2 - h ** 2) ** (1 / 2), h],
            [(a ** 2 - h ** 2) ** (1 / 2), h],
        )
        ax: Any = plt.gca()
        ax.set_aspect('equal')
        ax.set_xlim((-20, 20))
        ax.set_ylim((-20, 20))
        plot_rhombus = plt.Polygon(points, color="green", fill=False)
        ax.add_patch(plot_rhombus)


class RendererVolumeFigures:

    @staticmethod
    def get_plot_sphere(r):
        """
        Renderer a sphere
        :param float r: radius of the sphere
        """
        u: Any = np.linspace(0, 2 * math.pi, 100)
        v: Any = np.linspace(0, math.pi, 100)
        x: float = r * np.outer(np.cos(u), np.sin(v))
        y: float = r * np.outer(np.sin(u), np.sin(v))
        z: float = r * np.outer(np.ones(np.size(u)), np.cos(v))
        fig = plt.figure()
        ax = fig.add_subplot(111, projection="3d")
        ax.set_box_aspect([1, 1, 1])
        ax.plot_surface(x, y, z, color="green")

    @staticmethod
    def get_plot_cube(a):
        """
        Renderer a cube
        :param int a: side length of the cube
        """
        axes: List[int] = [a, a, a]
        data: Any = np.ones(axes, dtype=np.bool)
        fig: Any = plt.figure()
        ax: Any = fig.add_subplot(111, projection="3d")
        ax.set_box_aspect([1, 1, 1])
        ax.voxels(data, facecolors="green")

    @staticmethod
    def get_plot_parallelepiped(a, b, c):
        """
        Renderer a parallelepiped
        :param int a: side length of the rectangular parallelepiped
        :param int b: side length of the rectangular parallelepiped
        :param int c: side length of the rectangular parallelepiped
        """
        axes: List[int] = [a, b, c]
        data: Any = np.ones(axes, dtype=np.bool)
        fig: Any = plt.figure()
        ax: Any = fig.add_subplot(111, projection="3d")
        ax.voxels(data, facecolors="green")

    @staticmethod
    def get_plot_pyramid(a, h, n):
        """
        Renderer a pyramid
        :param float a: foundation side length of the right pyramid
        :param float h: length of the height of right pyramid
        :param int n: the number of parties to the base of right pyramid
        """
        r: float = a / (2 * np.sin(math.pi / n))
        X: List[float] = []
        Y: List[float] = []
        Z: Any = np.zeros(n + 1)
        Z[n] = h
        for i in range(0, n):
            x: float = r * np.cos((2 * math.pi * i) / n)
            y: float = r * np.sin((2 * math.pi * i) / n)
            X.append(x)
            Y.append(y)
        X.append(0)
        Y.append(0)
        fig: Any = plt.figure()
        ax: Any = fig.add_subplot(111, projection="3d")
        ax.set_box_aspect([1, 1, 1])
        ax.plot_trisurf(X, Y, Z, color="green")

    @staticmethod
    def get_plot_cylinder(r, h):
        """
        Renderer a cylinder
        :param float r: radius of the foundation of right cylinder
        :param float h: length of the height of right cylinder
        """
        u: Any = np.linspace(0, 2 * math.pi, 50)
        height: Any = np.linspace(0, h, 20)
        x: float = r * np.outer(np.sin(u), np.ones(np.size(height)))
        y: float = r * np.outer(np.cos(u), np.ones(np.size(height)))
        z: float = np.outer(np.ones(np.size(u)), height)
        fig: Any = plt.figure()
        ax: Any = fig.add_subplot(111, projection="3d")
        ax.set_box_aspect([1, 1, 1])
        ax.plot_surface(x, y, z, color="green")

    @staticmethod
    def get_plot_cone(r, h):
        """
        Renderer a cone
        :param float r: radius of the foundation of right cone
        :param float h: length of the height of right cone
        """
        theta: Any = np.linspace(0, 2 * math.pi, 90)
        radius: Any = np.linspace(0, r, 50)
        T, R = np.meshgrid(theta, radius)
        x: float = R * np.cos(T)
        y: float = R * np.sin(T)
        z: float = np.sqrt(x ** 2 + y ** 2) * (h / r)
        fig: Any = plt.figure()
        ax: Any = fig.add_subplot(111, projection="3d")
        ax.plot_surface(x, y, z, color="green")
        ax.set_box_aspect([1, 1, 1])
        ax.invert_zaxis()
