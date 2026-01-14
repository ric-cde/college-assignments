# Write a Python program that will swap two random letters in a string.
# Hint: Random letters means “letters with random index”
# random.randint(x,y) will return a randomnumber in the range fromx to y inclusive.
# You need to import random at the top of your program.
# You’ll also need to use slicing –splitting your string into substrings

import random

my_str = input("Enter a string: ")

new_str = ''

x = random.randint(0,len(my_str))
y = random.randint(0,len(my_str))
counter = 0

print("x = ", x, "or", my_str[x])
print("y = ", y, "or", my_str[y])

length = len(new_str)
for c in my_str:
    if counter == y:
        new_str = new_str + my_str[x]
    elif counter == x:
        new_str = new_str + my_str[y]
    else:
        new_str = new_str + c
    counter += 1
    print(new_str)

print(new_str)