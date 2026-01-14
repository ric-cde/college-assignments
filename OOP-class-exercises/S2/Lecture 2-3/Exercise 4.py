# Extend the class Person and add a method older which returns true or false if a person is older than another person

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def older(self, comparison):
        if self.age < comparison.age:
            return True
        else:
            return False

p1 = Person('Mick', 75, 'Male')
p2 = Person('Bob', 80, 'Male')

print("Is {}'s age ({}) older than {}'s age ({})?".format(p2.name, p2.age, p1.name, p1.age), p1.older(p2))

text ="Here's SOME, text. %£"
t = filter(str.isalnum, text.lower())
text = "".join(t)
print(text)