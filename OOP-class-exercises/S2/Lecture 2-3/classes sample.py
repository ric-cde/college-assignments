# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.address = {}
#
# p = Person('Richard', 50, {'city centre', 'dublin'})
#
# print(p.name, p.age, p.address)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "X, Y: {}, {}".format(self.x, self.y)

    def distance(self, other):
        return ((other.x - self.x)**2 + (other.y - self.y)**2)**0.5

    def movex(self, amount):
        self.x = self.x + amount

    def movey(self, amount):
        self.y = self.y + amount

    def move(self):
        self.x = float(input("New value for x: "))
        self.y = float(input("New value for y: "))


home = Point(52.960306, 6.026424)
work = Point(52.987382, -6.076866)

print(home.distance(work))

print(home, "\n", work)

home.movex(2.5)

print(home)

home.movey(20)

print(home)

home.move()

print(home)

    # def setx(self):
    #
    # def sety(self):
    #
    # def calc_difference(self):

