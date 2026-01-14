# Extend the class Person and add a method older which returns true or false if a person is older than another person


class Person:
    def __init__(self, n, age, gender):
        self.__name = n
        self.__age = age
        self.__gender = gender

    def older(self, comparison):
        print("Is {}'s age ({}) older than {}'s age ({})?".format(comparison.__name, comparison.__age, self.__name, self.__age))
        if self.__age < comparison.__age:
            print(True)
        else:
            print(False)

    def split_names(self):
        temp = self.__name.split()
        print(f"Forename: {temp[0]}, Surname: {' '.join(temp[1:])}")


p1 = Person('Mick Doyle Murphy', 75, 'Male')
p2 = Person('Bob Vance', 80, 'Male')

p1.split_names()
p1.older(p2)

# print("Is {}'s age ({}) older than {}'s age ({})?".format(p2.name, p2.age, p1.name, p1.age), p1.older(p2))
