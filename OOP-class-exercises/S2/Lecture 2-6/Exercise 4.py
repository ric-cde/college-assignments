# You can write a class to represent anything you want.
# For example, write a class to represent an Address –each address has a country, city, street name and house number.
# Modify your Person class to use Address objects instead of string for representing the address.


class Person:
    def __init__(self, n, age, gender, address):
        self.__name = n
        self.__age = age
        self.__gender = gender
        self.__addresses = []
        if address is not None:
            self.__addresses.append(address)

    def older(self, comparison):
        print("Is {}'s age ({}) older than {}'s age ({})?".format(comparison.__name, comparison.__age, self.__name, self.__age))
        if self.__age < comparison.__age:
            print(True)
        else:
            print(False)

    def add_address(self, address):
        self.__addresses.append(address)

    def display_addresses(self):
        output = ""
        for i, addr in enumerate(self.__addresses):
            output += "\n  Address " + str(i+1) + ": " + str(addr)
        return output

    def split_names(self):
        temp = self.__name.split()
        print(f"Forename: {temp[0]}, Surname: {' '.join(temp[1:])}, Addresses: {self.display_addresses()}")


class Address:
    def __init__(self, street, street2, city, county, country, postcode):
        self._street = street
        self._street2 = street2
        self._city = city
        self._county = county
        self._country = country
        self._postcode = postcode
        self._attributes = [self._street, self._street2, self._city, self ._county, self._country, self._postcode]

    def add_address(self):
        for i in self._street, self._street2, self._city, self._county, self._country, self._postcode:
            i = input("Enter " + i)

    def __str__(self):
        readout = ""
        attr_list = [a for a in self._attributes if a is not None]
        print(attr_list)
        for i, attr in enumerate(attr_list):
            if attr is not None:
                readout += attr
                if len(attr_list) - i > 1:
                    readout += ", "
        return readout

a2 = Address("Church road", None, None, "County Hertfordshire", "UK", "ALT 739E")

p1 = Person('Mick Doyle Murphy', 75, 'Male', a2)
p2 = Person('Bob Vance', 80, 'Male', None)


p1.split_names()
p1.older(p2)

a1 = Address("Dunbur", None, "Rathnew", "Wicklow", "Ireland", None)
print(a1)

p1.add_address(a1)
p1.add_address(a1)
p1.add_address(a1)

p1.split_names()