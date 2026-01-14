import math


class Polygon:
    def __init__(self, no_of_sides, colour):
        self._n = no_of_sides
        self._sides = [int(input("Enter side " + str(i + 1) + " : "))
                       for i in range(self._n)]
        self._colour = colour
        self._centre = [0, 0]

    def display_sides(self):
        for i in range(self._n):
            print("Side", i+1, "is", self._sides[i])

    def move(self, x, y):
        self._centre[0] += x
        self._centre[1] += y

    def __str__(self):
        return 'Polygon with '+str(self._n)+' sides: '+str(self._sides)


class Triangle(Polygon):
    def __init__(self, colour):
        Polygon.__init__(self, 3, colour)

    def area(self):
        a, b, c = self._sides
        s = (a + b + c) / 2
        return (s * (s-a) * (s-b) * (s-c)) ** 0.5


class Rectangle(Polygon):
    def __init__(self, colour):
        Polygon.__init__(self, 4, colour)
        a, b, c, d = self._sides
        while a != c or b != d:
            print("Error: not a rectangle")
            Polygon.__init__(self, 4, colour)
            a, b, c, d = self._sides

    def area(self):
        a, b, c, d = self._sides
        return a * b


class Square(Rectangle):
    def __init__(self, colour):
        Rectangle.__init__(self, colour)
        z = self._sides
        while z[0] != z[1] or z[1] != z[2] or z[2] != z[3]:
            print("Error: not a square")
            Rectangle.__init__(self, colour)
            z = self._sides

    def s_area(self):
        return self._sides[0] ** 2


class Circle(Polygon):
    def __init__(self, colour):
        Polygon.__init__(self, 1, colour)

    def area(self):
        return (self._sides[0] ** 2) * math.pi


t = Triangle('red')
print("Area is:", (t.area()))
print("Location is:", t._centre)
t.move(50,75)
print("Location is:", t._centre)
t.move(3.5,4.5)
print("Location is:", t._centre)

sq = Square('blue')
print(sq.s_area())

ci = Circle('blue')
print(ci.area())