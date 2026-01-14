class Polygon:
    def __init__(self, no_of_sides):
        self._n = no_of_sides
        self._sides = [int(input("Enter side " + str(i + 1) + " : "))\
                       for i in range(self._n)]

    def display_sides(self):
        for i in range(self._n):
            print("Side", i+1, "is", self._sides[i])

    def __str__(self):
        return 'Polygon with '+ str(self._n)+' sides: '+str(self._sides)

class Rectangle(Polygon):
    def __init__(self):
        Polygon.__init__(self,4)
        a, b, c, d = self._sides
        while a!=c or b!=d:
            print("Error: not a rectangle")
            Polygon.__init__(self,4)
            a, b, c, d = self._sides
    def print_area(self):
        a, b, c, d = self._sides
        area = a * b
        print('The area of the rectangle is ', area)

example = Rectangle()
example.print_area()