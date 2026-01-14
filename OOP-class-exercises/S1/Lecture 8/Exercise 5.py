# Write a Python function that takes a list of numbers and
# returns a new list containing only the even numbers from the first list

def even_splitter(my_list):
    new_list = []
    for i in my_list:
        if int(i) % 2 == 0:
            new_list.append(i)
    return new_list

my_list = input("Enter a list of numbers separated by spaces: ").split()
print(my_list)

new_list = even_splitter(my_list)

print(new_list)