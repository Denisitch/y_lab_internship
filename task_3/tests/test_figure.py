import unittest
import math
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


class MyTestCase(unittest.TestCase):
    def test_circle_perimeter(self):
        r = 1
        circle = Circle(r)
        circle_perimeter = circle.perimeter()
        self.assertEqual(circle_perimeter, 2 * math.pi * r)

    def test_circle_area(self):
        r = 1
        circle = Circle(r)
        circle_area = circle.area()
        self.assertEqual(circle_area, math.pi * r ** 2)

    def test_square_perimeter(self):
        a = 1
        square = Square(a)
        square_perimeter = square.perimeter()
        self.assertEqual(square_perimeter, 4 * a)

    def test_square_area(self):
        a = 1
        square = Square(a)
        square_area = square.area()
        self.assertEqual(square_area, a ** 2)

    def test_rectangle_perimeter(self):
        a, b = 1, 2
        rectangle = Rectangle(a, b)
        rectangle_perimeter = rectangle.perimeter()
        self.assertEqual(rectangle_perimeter, 2 * (a + b))

    def test_rectangle_area(self):
        a, b = 1, 2
        rectangle = Rectangle(a, b)
        rectangle_area = rectangle.area()
        self.assertEqual(rectangle_area, a * b)

    def test_triangle_perimeter(self):
        a, b, c = 1, 1, 1
        triangle = Triangle(a, b, c)
        triangle_perimeter = triangle.perimeter()
        self.assertEqual(triangle_perimeter, a + b + c)

    def test_triangle_area(self):
        a, b, c = 1, 1, 1
        p = a + b + c
        triangle = Triangle(a, b, c)
        triangle_area = triangle.area()
        self.assertEqual(triangle_area, math.sqrt(p * (p - a) * (p - b) * (p - c)))

    def test_trapezoid_middle_line(self):
        a, b, h = 1, 2, 2
        trapezoid = Trapezoid(a, b, h)
        trapezoid_middle_line = trapezoid.middle_line()
        self.assertEqual(trapezoid_middle_line, (a + b) / 2)

    def test_trapeze_area(self):
        a, b, h = 1, 2, 2
        trapezoid = Trapezoid(a, b, h)
        trapezoid_area = trapezoid.area()
        self.assertEqual(trapezoid_area, ((a + b) / 2) * h)

    def test_rhombus_perimeter(self):
        a, h = 2, 1
        rhombus = Rhombus(a, h)
        rhombus_perimeter = rhombus.perimeter()
        self.assertEqual(rhombus_perimeter, 4 * a)

    def test_rhombus_area(self):
        a, h = 2, 1
        rhombus = Rhombus(a, h)
        rhombus_area = rhombus.area()
        self.assertEqual(rhombus_area, a * h)

    def test_sphere_area(self):
        r = 1
        sphere = Sphere(r)
        sphere_area = sphere.area()
        self.assertEqual(sphere_area, 4 * math.pi * r ** 2)

    def test_sphere_volume(self):
        r = 1
        sphere = Sphere(r)
        sphere_volume = sphere.volume()
        self.assertEqual(sphere_volume, 4 / 3 * math.pi * r ** 3)

    def test_cube_area(self):
        a = 1
        cube = Cube(a)
        cube_area = cube.area()
        self.assertEqual(cube_area, 6 * a ** 2)

    def test_cube_volume(self):
        a = 1
        cube = Cube(a)
        cube_volume = cube.volume()
        self.assertEqual(cube_volume, a ** 3)

    def test_parallelepiped_area(self):
        a, b, c = 1, 2, 3
        parallelepiped = Parallelepiped(a, b, c)
        parallelepiped_area = parallelepiped.area()
        self.assertEqual(parallelepiped_area, 2 * (a * b + a * c + b * c))

    def test_parallelepiped_volume(self):
        a, b, c = 1, 2, 3
        parallelepiped = Parallelepiped(a, b, c)
        parallelepiped_volume = parallelepiped.volume()
        self.assertEqual(parallelepiped_volume, a * b * c)

    def test_pyramid_area(self):
        a, h, n = 1, 4, 4
        pyramid = Pyramid(a, h, n)
        pyramid_area = pyramid.area()
        self.assertEqual(pyramid_area, (n * a / 2) * ((a / (2 * math.tan(math.pi / n)) + math.sqrt(
            h ** 2 + (a / (2 * math.tan(math.pi / n))) ** 2))))

    def test_pyramid_volume(self):
        a, h, n = 1, 4, 4
        pyramid = Pyramid(a, h, n)
        pyramid_volume = pyramid.volume()
        self.assertEqual(pyramid_volume, (n * (a ** 2) * h) / 12 * math.tan(math.pi / n))

    def test_cylinder_area(self):
        r, h = 1, 2
        cylinder = Cylinder(r, h)
        cylinder_area = cylinder.area()
        self.assertEqual(cylinder_area, 2 * math.pi * r * (r + h))

    def test_cylinder_volume(self):
        r, h = 1, 2
        cylinder = Cylinder(r, h)
        cylinder_volume = cylinder.volume()
        self.assertEqual(cylinder_volume, math.pi * (r ** 2) * h)

    def test_cone_area(self):
        r, h = 1, 2
        cone = Cone(r, h)
        cone_area = cone.area()
        g = (r**2 + h**2) ** (1 / 2)
        self.assertEqual(cone_area, math.pi * r * (r + g))

    def test_cone_volume(self):
        r, h = 1, 2
        cone = Cone(r, h)
        cone_volume = cone.volume()
        self.assertEqual(cone_volume, 1 / 3 * math.pi * (r ** 2) * h)
