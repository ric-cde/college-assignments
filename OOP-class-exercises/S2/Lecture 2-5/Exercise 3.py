# Using the BankAccount class from few weeks ago design classes for SavingsAccount and CurrentAccount.
# SavingsAccount has an interest rate and a method to calculate interest.
# CurrentAccount has an overdraft.
# Make sure you override any necessary methods in the BankAccount class
# Create a list of BankAccount objects –some SavingsAccount, some CurrentAccount.
# Write a update() function that iterates through each account, updating it in the following ways:
#   SavingsAccounts get interest added (via the method you already wrote)
#   CurrentAccounts get a letter sent if they are in overdraft
from random import randint


class BankAccount:
    def __init__(self, balance):
        self._balance = balance * 100

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
        return str(self._balance / 100)


class SavingsAccount(BankAccount):
    def __init__(self, balance, int_rate):
        BankAccount.__init__(self, balance)
        self._int_rate = int_rate

    def calc_int(self):
        interest = int(self._balance * self._int_rate / 100)
        self._balance += interest
        print(f"    {interest/100} in interest @ {self._int_rate}% added to account")
        self.show_balance()

    def __str__(self):
        return str(f"Balance: {self._balance/100} | Interest rate: {self._int_rate}%")


class CurrentAccount(BankAccount):
    def __init__(self, balance, overdraft):
        BankAccount.__init__(self, balance)
        self._overdraft = overdraft * 100

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
        return str(f"Balance: {self._balance/100} | Overdraft: {self._overdraft/100}")


def update(account_list):
    print("Updating accounts...")
    for a in account_list:
        print("  "+str(a))
        if type(a) == SavingsAccount:
            a.calc_int()
        else:
            a.overdraft()


my_account = SavingsAccount(0, 5)

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

accounts = []
s_rate = 7.5
overdraft = 250

print("Listing new accounts...")
for i in range(0, randint(5, 10)):
    if randint(0, 1) == 0:
        n_balance = randint(0, 9750)
        accounts.append(SavingsAccount(n_balance, s_rate))
    else:
        n_balance = randint(-250, 250)
        accounts.append(CurrentAccount(n_balance, overdraft))
    print(accounts[i])
print(" ~ ")
update(accounts)
