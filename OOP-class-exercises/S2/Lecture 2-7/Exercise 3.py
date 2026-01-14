# Write a class to represent  a car – each car has reg number, make, engine size and four wheels.
# Each wheel has tread depth. A car is safe is the tread depth of each four wheels is at least 1.6mm.
# A Garage may have several cars. Add functionality that alerts the garage which cars need their wheels replaced.

import random


class Garage:
    def __init__(self):
        self._cars = []

    def add_car(self, car):
        self._cars.append(car)

    def check_car_wheels(self):
        for car in self._cars:
            check = car.check_wheel_depth()
            if check:
                print(f"A {car._make} ({car._reg}) has {len(check)} bare tires. These wheels need to replaced: ")
                for wheel in check:
                    print("    Tyre #" + str(wheel) + " (" + str(check[wheel]) + "mm)")
            else:
                print("All tires at minimum depth of 1.6mm")
            if len(car._wheels) < 4:
                print(f"This car is missing {4 - len(car._wheels)} wheels")


class Car:
    def __init__(self, reg, make, engine, wheels):
        self._reg = reg
        self._make = make
        self._engine = engine
        self._wheels = []
        self._wheels += wheels

    def check_wheel_depth(self):
        thin_wheels = {}
        for i, wheel in enumerate(self._wheels):
            if wheel < 1.6:
                thin_wheels[i] = wheel
        if thin_wheels:
            return thin_wheels
        else:
            return False

    def add_wheel(self, wheels):
        if len(self._wheels) < 4:
            for wheel in wheels:
                while len(self._wheels) < 4:
                    self._wheels.append(wheel)   #  What if there are more wheels to add beyond max?
        else:
            print("This car already has 4 wheels.")

    def rem_wheel(self, num):
        if self._wheels[int(num)]:
            self._wheels.pop(int(num))
            print(f"Wheel #{num} removed")
        else:
            print("No wheel of that number exists.")


class Wheel:
    def __int__(self, depth):
        self._thread_depth = depth

    def __str__(self):
        return str(self._thread_depth)


my_garage = Garage()


def generate_wheels():
    temp_wheels = []
    for i in range(random.randint(2, 8)):
        temp_wheels.append(round(random.uniform(0.85, 4.0), 2))
    return temp_wheels


my_garage.add_car(Car("153wz1066", "Nissan", "Electric", generate_wheels()))
my_garage.check_car_wheels()


