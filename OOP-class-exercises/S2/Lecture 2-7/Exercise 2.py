# Design classes in Python to represent generic Animals,  as well as Cats and Dogs.
# Each animal has a name and can make a sound.
# Write a small test program to test your clas
# Write a class for a Zoo, each zoo has a name, address and a list of animals.
# Add a method in your zoo class that will list details for each animals you have – their name and the sound they make.


class Zoo:
    def __init__(self, name, address, stock):
        self._name = name
        self._address = address
        self._stock = []
        if stock is not None:
            self._stock += stock

    def list_animals(self):
        animal_list = ""
        for animal in self._stock:
            animal_list += str(animal) + "\n"
        return animal_list


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
        return "miaows!"

    def __str__(self):
        return f"{self._name} ({self._age}) {self.make_noise()}"
        # return " ".join([self.__class__.__name__ + ",", self._name, str(self._age)])


class Dog(Animal):
    def __init__(self, name, age, spots):
        Animal.__init__(self, name, age)
        self.__spots = spots

    def make_noise(self):
        return "barks!"

    def __str__(self):
        return f"{self._name} ({self._age}) {self.make_noise()}"

class Bird(Animal):
    def __init__(self, name, age, feathers):
        Animal.__init__(self, name, age)
        self.__feathers = feathers

    def make_noise(self):
        return "chirps!"

    def __str__(self):
        return f"{self._name} ({self._age}) {self.make_noise()}"

zig = Cat("Zig", 10, True)
print(zig)

barky = Dog("Barky", 3, True)
print(barky)

tweety = Bird("Tweety Bird", 5, True)
print(tweety)

my_zoo = Zoo("Central Pork", "1000 Avenue of the 10000s", [zig, barky, tweety])

print(my_zoo.list_animals())