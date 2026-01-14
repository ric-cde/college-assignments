# Week 6 Aggregation / Composition


# We-write the shapes classes from couple of weeks ago and instead of using two numbers, x and y,
# for the coordinates of the share, use an object of class Point instead

import math


class Polygon:
    def __init__(self, no_of_sides, colour):
        self._n = no_of_sides
        self._sides = [int(input("Enter side " + str(i + 1) + " : ")) \
                       for i in range(self._n)]
        self._colour = colour
        self._points = []

    def display_sides(self):
        for i in range(self._n):
            print("Side", i + 1, "is", self._sides[i])

    def add_points(self, p):
        self._points.append(p)

    def get_points(self):
        return [str(x) for x in self._points]

    def __str__(self):
        return 'Polygon with ' + str(self._n) + ' sides: ' + str(self._sides)


class Circle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 1, input("Colour: "))

    def print_area(self):
        area = (self._sides[0] ** 2) * math.pi
        print('The area of the circle is ', area, '\nThe colour is ', self._colour)


class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def set_x(self, new_x):
        self._x = new_x

    def set_y(self, new_y):
        self._y = new_y

    def __str__(self):
        return str(self._x)+","+str(self._y)
        #return (f"X: {self._x} Y: {self._y}")


example = Circle()
p1 = Point(5, 4)
p2 = Point(18, 2)
print(p1)
print(p2)
example.add_points(p1)
example.add_points(p2)
print(example.get_points())

example.print_area()

