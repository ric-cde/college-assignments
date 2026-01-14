# Write a Python program that will calculate the length of a string (We already have a function lenthat does that, but we want to implement our own)

my_str = input("Enter a string: ")

count = 0

for c in my_str:
    count += 1

print(count)