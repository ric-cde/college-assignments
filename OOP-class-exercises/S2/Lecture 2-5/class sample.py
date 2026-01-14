class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def __str__(self):
        return str(self.__name)+" "+str(self.__age)
        # return ' '.join([self.__name, str(self.__age)])


class Student(Person):
    def __init__(self, name, age, student_number, courses):
        Person.__init__(self, name, age)
        self.__student_number = student_number
        self.__courses = courses

    def __str__(self):
        attributes = map(str, [self._Person__name, str(self._Person__age), self.__courses, self.__student_number])
        return ' '.join(attributes)


class Staff(Person):
    def __init__(self, name, age, office_number):
        Person.__init__(self, name, age)
        self.__office_number = office_number

    def __str__(self):
        attributes = map(str, [self._Person__name, str(self._Person__age), self.__office_number])
        return ' '.join(attributes)


m = Student('Richard', 33, 55585830, 'Forestry')
print(m)

n = Staff('Rachael', 40, 14)
print(n)