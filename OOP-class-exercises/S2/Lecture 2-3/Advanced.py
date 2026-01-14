# Write a class Student. Every student should have a name, student number and a list of marks
# (implemented as a python list) Include any appropriate methods, and a method to calculate the average mar

class Student:
    def __init__(self, name, number, marks):
        self.name = name
        self.number = number
        self.marks = marks
    def average_mark(self):
        total = 0
        for mark in self.marks:
            total += mark
        return total / len(self.marks)

    def compare_mark(self, comparison):
        if self.average_mark() > comparison.average_mark():
            return("{} has better marks".format(self.name))
        else:
            return("{} has better marks".format(comparison.name))

s1 = Student('Kevin', 53, [90, 50, 60])
s2 = Student('Mick', 54, [80, 34, 150])

print("{}'s marks: ".format(s1.name), s1.marks, "\nAverage:", round(s1.average_mark(), 2))
print("{}'s marks: ".format(s2.name), s2.marks, "\nAverage:", round(s2.average_mark(), 2))

print(s1.compare_mark(s2))