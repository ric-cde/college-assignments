# Design classes in Python to represent generic Animals,  as well as Cats and Dogs.
# Each animal has a name and can make a sound.
# Write a small test program to test your clas

class Animal:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def __str__(self):
        return str(self._name)+" "+str(self._age)


geoff = Animal('Geoff', 27)
print(geoff)


class Cat(Animal):
    def __init__(self, name, age, whiskers):
        Animal.__init__(self, name, age)
        self.__whiskers = whiskers

    def make_noise(self):
        return self._name + " miaows!"

    def __str__(self):
        return " ".join([self.__class__.__name__ + ",", self._name, str(self._age)])


class Dog(Animal):
    def __init__(self, name, age, spots):
        Animal.__init__(self, name, age)
        self.__spots = spots

    def make_noise(self):
        return self._name + " barks!"

    def __str__(self):
        return " ".join([self.__class__.__name__ + ",", self._name, str(self._age)])

zig = Cat("Zig", 10, True)
print(zig)
print(zig.make_noise())

barky = Dog("Barky", 3, True)
print(barky)
print(barky.make_noise())