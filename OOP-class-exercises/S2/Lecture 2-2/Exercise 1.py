# Exercise 1: Write a Python program to create a list of contact details – using name, phone number and office number as
# in the example in the class.
# Write a function that takes a dictionary and an office number, and prints the names of all people in that office

def dict_print(in_dict, office_num):
    for key in in_dict:
        if in_dict[key][1] == office_num:
            print(key)

contacts = {
    'Michael': ['01-9448493', 'A1'],
    'Siobhan': ['01-9448342', 'A2'],
    'Kerry': ['01-9448494', 'A1'],
    'Philip': ['01-94484293', 'B1'],
}

# print(contacts)

dict_print(contacts, 'A1')

# for key in contacts:
    print(f"{key}: {contacts[key][0]} - {contacts[key][1]}")

