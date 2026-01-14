# Exercise 2: Using the contact list from Exercise 1 write a python function that prints
# all people whose name begins with a specific character. Your function will take two
# parameters – the character and the dictionary

def dict_print(in_dict, letter):
    for key in in_dict:
        if key[0].lower() == letter.lower():
            print(key)

contacts = {
    'Michael': ['01-9448493', 'A1'],
    'Siobhan': ['01-9448342', 'A2'],
    'Merry': ['01-9448494', 'A1'],
    'Philip': ['01-94484293', 'B1'],
}



dict_print(contacts, input("Enter a letter"))