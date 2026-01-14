# Write a Python program that will “encrypt” a string.
# The encryption algorithm we’ll use is add 1 to the ASCII code, so ‘a’ becomes ‘b’, ‘b’ becomes ‘c’, etc.
# The string ‘abc’ becomes ‘bcd’
# You’ll need to use the functions ord() and chr() discussed in class
# Hint: To encrypt the letter ‘a’ take the ASCII code of ‘a’ 97, add 1 (98)and find the character with ASCII code 98 (‘b’). So ‘a’ encrypted becomes ‘b’

my_str = input("Enter a phrase to be encrypted: ")

new_str = ''

for c in my_str:
    new_str = new_str + chr(ord(c) + 1)

print(new_str)