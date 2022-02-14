"""The module contains classes of flat and volumetric figures."""

import math


class Figure:
    """This is an abstract figure class."""

    title = "Фигура"

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if value <= 0:
                raise ValueError("Parameters can't be negative")
            setattr(self, key, value)

    def area(self):
        raise NotImplementedError("Abstract figure. Area is not defined.")

    @classmethod
    def figure_name(cls):
        return cls.title


class FlatFigure(Figure):
    """This is an abstract flat figure class."""

    title = "Плоская фигура"

    def perimeter(self):
        raise NotImplementedError("Abstract figure. Perimeter is not defined.")

    def area(self):
        raise NotImplementedError("Abstract figure. Area is not defined.")


class VolumetricFigure(Figure):
    """This is an abstract volumetric figure class."""

    title = "Объемная фигура"

    def area(self):
        raise NotImplementedError("Abstract figure. Area is not defined.")

    def volume(self):
        raise NotImplementedError("Abstract figure. Volume is not defined.")


class Circle(FlatFigure):
    """
    This class describes circle.

    :param float r: radius of the circle
    """

    title = "Круг"

    def __init__(self, r):
        super().__init__(r=r)

    @property
    def perimeter(self):
        return 2 * math.pi * self.r

    @property
    def area(self):
        return math.pi * self.r**2

    def __str__(self):
        return (
            f'{self.figure_name()}'
            f'radius r'
        )


class Square(FlatFigure):
    """
    This class describes square.

    :param float a: side length of the square
    """

    title = "Квадрат"

    def __init__(self, a):
        super().__init__(a=a)

    @property
    def perimeter(self):
        return 4 * self.a

    @property
    def area(self):
        return self.a**2


class Rectangle(FlatFigure):
    """
    This class describes rectangle.

    :param float a: side length of the rectangle
    :param float b: side length of the rectangle
    """

    title = "Прямоугольник"

    def __init__(self, a, b):
        super().__init__(a=a, b=b)

    @property
    def perimeter(self):
        return 2 * (self.a + self.b)

    @property
    def area(self):
        return self.a * self.b


class Triangle(FlatFigure):
    """
    This class describes triangle.

    :param float a: side length of the triangle
    :param float b: side length of the triangle
    :param float c: side length of the triangle
    """

    title = "Треугольник"

    def __init__(self, a, b, c):
        super().__init__(a=a, b=b, c=c)
        if a + b <= c or a + c <= b or b + c <= a:
            raise AttributeError("Triangle does not exist")

    @property
    def perimeter(self):
        return self.a + self.b + self.c

    @property
    def area(self):
        p = self.perimeter
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))


class Trapezoid(FlatFigure):
    """
    This class describes trapeze.

    :param float a: side length of the trapeze
    :param float b: side length of the trapeze
    :param float h: length of the height of trapeze
    """

    title = "Трапеция"

    def __init__(self, a, b, h):
        super().__init__(a=a, b=b, h=h)

    @property
    def perimeter(self):
        pass

    @property
    def middle_line(self):
        return (self.a + self.b) / 2

    @property
    def area(self):
        return ((self.a + self.b) / 2) * self.h


class Rhombus(FlatFigure):
    """
    This class describes rhombus.

    :param float a: side length of the rhombus
    :param float h: length of the height of rhombus
    """

    title = "Ромб"

    def __init__(self, a, h):
        super().__init__(a=a, h=h)

    @property
    def perimeter(self):
        return 4 * self.a

    @property
    def area(self):
        return self.a * self.h


class Sphere(VolumetricFigure):
    """
    This class describes sphere.

    :param float r: radius of the sphere
    """

    title = "Сфера"

    def __init__(self, r):
        super().__init__(r=r)

    @property
    def area(self):
        return 4 * math.pi * self.r**2

    @property
    def volume(self):
        return 4 / 3 * math.pi * self.r**3


class Cube(VolumetricFigure):
    """
    This class describes cube.

    :param int a: side length of the cube
    """

    title = "Куб"

    def __init__(self, a):
        super().__init__(a=a)

    @property
    def area(self):
        return 6*self.a**2

    @property
    def volume(self):
        return self.a**3


class Parallelepiped(VolumetricFigure):
    """
    This class describes rectangular parallelepiped.

    :param int a: side length of the rectangular parallelepiped
    :param int b: side length of the rectangular parallelepiped
    :param int с: side length of the rectangular parallelepiped
    """

    title = "Параллелепипед"

    def __init__(self, a, b, c):
        super().__init__(a=a, b=b, c=c)

    @property
    def area(self):
        return 2 * (self.a * self.b + self.a * self.c + self.b * self.c)

    @property
    def volume(self):
        return self.a * self.b * self.c


class Pyramid(VolumetricFigure):
    """
    This class describes right pyramid.

    :param float a: foundation side length of the right pyramid
    :param float h: length of the height of right pyramid
    :param int n: the number of parties to the base of right pyramid
    """

    title = "Пирамида"

    def __init__(self, a, h, n):
        super().__init__(a=a, h=h, n=n)

    @property
    def area(self):
        return (self.n * self.a / 2) * (
            (
                self.a / (2 * math.tan(math.pi / self.n))
                + math.sqrt(
                    self.h**2 + (self.a / (2 * math.tan(math.pi / self.n))) ** 2
                )
            )
        )

    @property
    def volume(self):
        return (self.n * (self.a**2) * self.h) / 12 * math.tan(math.pi / self.n)


class Cylinder(VolumetricFigure):
    """
    This class describes right cylinder.

    :param float r: radius of the foundation of right cylinder
    :param float h: length of the height of right cylinder
    """

    title = "Цилиндр"

    def __init__(self, r, h):
        super().__init__(r=r, h=h)

    @property
    def area(self):
        return 2 * math.pi * self.r * (self.r + self.h)

    @property
    def volume(self):
        return math.pi * (self.r**2) * self.h


class Cone(VolumetricFigure):
    """
    This class describes right cone.

    :param float r: radius of the foundation of right cone
    :param float h: length of the height of right cone
    """

    title = "Конус"

    def __init__(self, r, h):
        super().__init__(r=r, h=h)

    @property
    def area(self):
        g = (self.r**2 + self.h**2) ** (1 / 2)
        return math.pi * self.r * (self.r + g)

    @property
    def volume(self):
        return 1 / 3 * math.pi * (self.r**2) * self.h
