# 1. Add a small menu system to the example 1 from last class (Employee class) to add, delete, etc employees.

# Write a class to represent a Salary – salary object has monthly pay amount and a yearly bonus.
# Add a method to calculate annual pay.

class Salary:
    def __init__(self, monthly, bonus):
        self.__monthly = monthly
        self.__bonus = bonus

    def get_monthly_salary(self):
        return self._monthly

    def annual_pay(self):
        return (self.__monthly * 12) + self.__bonus

    def modify_pay(self, amount):
        self.__monthly *= (1 + (amount/100))

    def __str__(self):
        return "Monthly pay: " + str(self.__monthly) + ", Bonus: " + str(self.__bonus)

# Write a class for Employee – each employee has a name, age and a salary (use your salary class).
# Add any necessary methods.

class Employee:
    def __init__(self, name, age, monthly, bonus):
        self.__name = name
        self.__age = age
        self.__salary_obj = Salary(monthly, bonus)
        # Salary.__init__(self, monthly, bonus)

    def get_name(self):
        return self.__name

    def annual_pay(self):
        return self.__salary_obj.annual_pay()

    def modify_pay(self, amount):
        self.__salary_obj.modify_pay(amount)

    def set_age(self, new_age):
        self.__age = new_age

    def __str__(self):
        return self.__name + ", " + str(self.__age) + ", " + str(self.__salary_obj) + ", Annual pay: " + \
               str(self.annual_pay())

# Write a class Company – each company has a name and a list of employees.
# Add a method to calculate the total pay to all employees per year.
# Add a functionality to increase everybody’s monthly pay by 5%, and calculate the total pay for the company again.


class Company:
    def __init__(self, name):
        self.__name = name
        self.__employees = []

    def add_employee(self, name, age, monthly, bonus):
        e = Employee(name, age, monthly, bonus)
        self.__employees.append(e)

    def print_all_employees(self):
        for e in self.__employees:
            print(e)

    def total_pay(self):
        total = 0
        for e in self.__employees:
            total += e.annual_pay()
        return total

    def modify_pay(self, amount):
        for e in self.__employees:
            e.modify_pay(amount)

    def find_employee(self, name):
        for e in self.__employees:
            if e.get_name() == name:
                return e
        return None

    def delete_employee(self, name):
        e = self.find_employee(name)
        if e in self.__employees:
            self.__employees.remove(e)
            print(f"{e.get_name()} deleted.")
        else:
            print("No such employee to delete.")

    def menu(self):
        option = "0"
        while option != "5":
            print("Menu operations: \n 1. Add employee\n 2. Delete employee\n 3. Print all employees\n"
                  " 4. Update employee's age\n 5. Exit")

            option = input("Please enter an option:")
            if option == "1":
                print("Adding a new employee ")
                name = input("Please enter a name:")
                age = int(input("Please enter an age:"))
                monthly_pay = int(input("Please enter monthly pay:"))
                bonus = int(input("Please enter a bonus:"))
                self.add_employee(name, age, monthly_pay, bonus)
            elif option == "2":
                print("Deleting employee...")
                name = input("Enter name: ")
                self.delete_employee(name)
            elif option == "3":
                self.print_all_employees()
            elif option == "4":
                name = input("Enter the name of the employee you want to update: ")
                e = self.find_employee(name)
                new_age = int(input("Enter new age for the employee"))
                e.set_age(new_age)
            else:
                print("Invalid option")




richard = Employee("Richard", 33, 1500, 1000)
print(richard)


prog_wizz = Company("Programming Wizz")
prog_wizz.add_employee("Mark", 30, 2500, 1000)
prog_wizz.add_employee("Mary", 35, 2800, 1500)

prog_wizz.print_all_employees()
print("Total pay for everybody: ", prog_wizz.total_pay())

prog_wizz.modify_pay(5)
print("Increasing pay...")
print("Total pay for everybody: ", prog_wizz.total_pay())

prog_wizz.menu()