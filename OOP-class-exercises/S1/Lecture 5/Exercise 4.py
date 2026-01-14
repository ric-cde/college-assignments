# Write a Python program that will reverse a string (using a loop, not using slicing)

my_str = input("Enter a string: ")

counter = -1

new_str = ''

for c in my_str:
    new_str = c + new_str
    print(new_str)

# i = len(my_str) - 1
#
# i = 4
#
# new_str = ''
#
# while i >= 0:
#     new_str = new_str + my_str[i]
#     # print(my_str[i])
#     i -= 1
#
# print(new_str)

#for c in my_str:
#    new_str = new_str + my_str
#    print(my_str[counter], end ="")
#    counter -= 1

#for i in range(len(my_str)-1, -1, -1):
#    print(new_str[i]) + my_str[i]