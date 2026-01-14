# Ask the user to enter a number andprint it back on the screen. Keep asking for a new number until they enter a negative number.

num = int(input("Enter a number: "))

while num >= 0:
# while num < 0 or num > 10:
    num = int(input("Number must be negative "))
    print(num)

print("Success!")

