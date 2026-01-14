# Write a Python function to sum all numbers in a list

def listsum(input_list):
    count = 0
    for i in input_list:
        count += int(i)
    return count

my_list = input("Enter a list of numbers separated by spaces: ").split()

my_list.sort()

print(my_list)

print("Sum of the list is", listsum(my_list))

#
