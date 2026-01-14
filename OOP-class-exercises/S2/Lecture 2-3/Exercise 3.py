# Write a class BankAccount. Every bank account has a balance. Include methods to deposit and withdraw money


class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Error: insufficient balance.")
        else:
            self.balance -= amount

my_account = BankAccount(0)

current = 1

while current != 0:
    current = int(input("Press 1 to see balance, 2 to deposit, 3 to withdraw, 0 to exit\n"))
    if current == 1:
        print(my_account.balance)
    elif current == 2:
        my_account.deposit(int(input("Enter amount to deposit: ")))
        print("New balance is:", my_account.balance)
    elif current == 3:
        my_account.withdraw(int(input("How much to withdraw: ")))
        print("New balance is:", my_account.balance)
