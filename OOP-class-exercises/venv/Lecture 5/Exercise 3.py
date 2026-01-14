# Write a Python program that reads a string and prints a sting that is made up of the first two characters and the last two characters.
# If the string has a length less than 4 the program prints a message on the screen.
# For example: “hello there” will result in “here

my_str = input("Enter a string: ")

if len(my_str) < 4:
    print("You must enter at least 5 letters.")

print(my_str[ : 2])
print(my_str[-2 : ])