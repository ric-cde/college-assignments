# Using the bank account classes we developed few weeks ago, write a class Bank.
# Every bank has a name, a list of savings accounts, and a list of current account


class Bank:
    def __init__(self, name):
        self._name = name
        self._saving_accounts = []
        self._current_accounts = []

    def add_savings(self, account):
        self._saving_accounts.append(account)

    def add_current(self, account):
        self._current_accounts.append(account)

    def display_accounts(self, accounts):
        result = "\n"
        for n, a in enumerate(accounts):
            result = result + " * " + str(a) + "\n"
            # if len(accounts) - n > 1:
            #     result += ", "
        return result

    def __str__(self):
        return f"There are {len(self._saving_accounts)} saving accounts and {len(self._current_accounts)} current " \
               f"accounts. \n\nList of savings accounts: {self.display_accounts(self._saving_accounts)}\n" \
               f"List of current accounts: {self.display_accounts(self._current_accounts)}"


from random import randint


class BankAccount:
    def __init__(self, balance, name):
        self._balance = balance * 100
        self._name = name

    def deposit(self, amount):
        self._balance += int(amount * 100)

    def withdraw(self, amount):
        withdrawal = int(amount * 100)
        if withdrawal > self._balance:
            print("Error: insufficient balance.")
        else:
            self._balance -= withdrawal

    def show_balance(self):
        print(f"    Current balance is {self._balance / 100}")

    def __str__(self):
        return str("{self._name} | Balance: {self._balance/100}")


class SavingsAccount(BankAccount):
    def __init__(self, balance, name, int_rate):
        BankAccount.__init__(self, balance, name)
        self._int_rate = int_rate
        self._name = name

    def calc_int(self):
        interest = int(self._balance * self._int_rate / 100)
        self._balance += interest
        print(f"    {interest/100} in interest @ {self._int_rate}% added to account")
        self.show_balance()

    def __str__(self):
        return str(f"{self._name} | Balance: {self._balance/100} | Interest rate: {self._int_rate}%")


class CurrentAccount(BankAccount):
    def __init__(self, balance, name, overdraft):
        BankAccount.__init__(self, balance, name)
        self._overdraft = overdraft * 100
        self._name = name

    def withdraw(self, amount):
        withdrawal = int(amount * 100)
        if withdrawal > self._balance + self._overdraft:
            print("Error: insufficient balance.")
        else:
            self._balance -= withdrawal

    def overdraft(self):
        if self._balance < 0:
            print(f"    Account is in overdraft. Current balance: {self._balance/100}. Maximum overdraft: {self._overdraft/100}")
            print("    Issuing letter to account holder...")

    def __str__(self):
        return str(f"{self._name} | Balance: {self._balance/100} | Overdraft: {self._overdraft/100}")


def update(account_list):
    print("Updating accounts...")
    for a in account_list:
        print("  "+str(a))
        if type(a) == SavingsAccount:
            a.calc_int()
        else:
            a.overdraft()


my_account = SavingsAccount(0, "Will Smith", 5)

current = 1

while current != 0:
    current = int(input("Press 1 to see balance, 2 to deposit, 3 to withdraw, 0 to exit\n"))
    if current == 1:
        my_account.show_balance()
    elif current == 2:
        my_account.deposit(float(input("Enter amount to deposit: ")))
        my_account.show_balance()
    elif current == 3:
        my_account.withdraw(float(input("How much to withdraw: ")))
        my_account.show_balance()

my_account.calc_int()

s_accounts = []
s_rate = 7.5
s_overdraft = 250

print("Listing new accounts...")
for i in range(0, randint(5, 10)):
    if randint(0, 1) == 0:
        n_balance = randint(0, 9750)
        s_accounts.append(SavingsAccount(n_balance, "Test Savings", s_rate))
    else:
        n_balance = randint(-250, 250)
        s_accounts.append(CurrentAccount(n_balance, "Test Current", s_overdraft))
    print(s_accounts[i])
print(" ~ ")
update(s_accounts)

#
# class BankAccount:
#     def __init__(self, balance, name):
#         self.balance = balance
#         self.name = name
#
#     def deposit(self, amount):
#         self.balance += amount
#
#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("Error: insufficient balance.")
#         else:
#             self.balance -= amount
#

a1 = SavingsAccount(0, "Will Smith", 7)
a2 = SavingsAccount(0, "DJ Jazzy Jeff", 9)
b1 = Bank("Bank of Hibernia")

b1.add_savings(a1)
b1.add_savings(a2)

print(b1)

for ac in s_accounts:
    if type(ac) == SavingsAccount:
        b1.add_savings(ac)
    if type(ac) == CurrentAccount:
        b1.add_current(ac)

print(b1)


# current = 1
#
# while current != 0:
#     current = int(input("Press 1 to see balance, 2 to deposit, 3 to withdraw, 0 to exit\n"))
#     if current == 1:
#         print(my_account.balance)
#     elif current == 2:
#         my_account.deposit(int(input("Enter amount to deposit: ")))
#         print("New balance is:", my_account.balance)
#     elif current == 3:
#         my_account.withdraw(int(input("How much to withdraw: ")))
#         print("New balance is:", my_account.balance)
