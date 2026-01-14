# Write a Python function to get the largest number from a list.

def large_num(my_int):
    return max(my_int)

my_list = input("Enter list of numbers separated by spaces").split()
print(my_list)

print(large_num(my_list))
