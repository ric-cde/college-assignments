# Write a Python class to represent a rectangle. Include methods to calculate the area and paramete

class Rectangle:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def area(self):
        return self.x * self.y

    def perimeter(self):
        return 2 * (self.x + self.y)

example = Rectangle(input("Width: "), input("Height: "))

# print(example.area())

print("The area is:", example.area())
print("The perimeter is:", example.perimeter())