# 1. Write a Python script to sort (ascending and descending) a dictionary by value. Go to the editor

import operator

contacts = {
    'Cerwyn': 'Wales',
    'Siobhan': 'Ireland',
    'Avery': 'England',
    'Miles': 'Scotland'
}

def sort_list(in_dict):
    print("Before: ", in_dict)
    in_dict = dict(sorted(in_dict.items(), key=operator.itemgetter(1)))
    return in_dict

contacts = sort_list(contacts)
print("After: ", contacts)
#for key in contacts:

# 2. Write a Python script to add a key to a dictionary. Go to the editor

# newName = input("Enter a name: ")
# newCountry = input("Enter a country: ")
# contacts[newName] = newCountry
#
# print(contacts)

# 3. Write a Python script to concatenate following dictionaries to create a new one. Go to the editor

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}

dic1.update(dic2)
dic1.update(dic3)

print(dic1)

# 4. Write a Python script to check whether a given key already exists in a dictionary. Go to the editor

if 5 in dic1:
    print("5 exists")


# 5. Write a Python program to iterate over dictionaries using for loops. Go to the editor

for key, value in dic1.items():
    print(key, "->", value)

# 6. Write a Python script to generate and print a dictionary that contains a number
# (between 1 and n) in the form (x, x*x). Go to the editor

def gen_dict(n):
    numbers = {}
    for i in range(1, n+1):
        numbers[i] = i*i
    return numbers

print(gen_dict(5))
