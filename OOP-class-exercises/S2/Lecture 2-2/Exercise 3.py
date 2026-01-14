# Exercise3: Write a Python program to create a list of items and corresponding quantities,
# e.g.


inventory = { 'apple':20, 'banana':30, 'orange':10}

def sum_dict(in_dict):
    total = 0
    for key in inventory:
        total += in_dict[key]
    return total

print(f"Total of inventory is {sum_dict(inventory)}")


def stock_up(dict, in_key, up_value):
    if in_key in dict:
        dict[in_key] = dict[in_key] + up_value
        print(f"Current value of {in_key} is {dict[in_key]}")
    else:
        dict[in_key] = up_value

stock_up(inventory, 'banana', 25)