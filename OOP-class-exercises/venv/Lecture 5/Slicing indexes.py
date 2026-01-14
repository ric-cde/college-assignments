hello = 'Hello, and welcome to an example.'

print(hello[5], " = ,")
print(hello[-1], " = .")
#hello[-1] = 'Q'
#print(hello[-1] , " = Q")
print(hello[ : ], " = .")
print(hello[3 : ], " = l to .")
print(hello[ : 8], " = a")
print(hello[5 : -5], " = , to a")


my_str = 'Hello'
new_str = my_str[:]
other_str = my_str
print("\n"+new_str)
print(other_str)

print("\n",new_str + "%%%" +other_str)

print("\n",new_str * 15)

print(my_str[::-2])
print(my_str[::-1])

print(my_str[1:6:2])

my_str.upper()

print("\n" + my_str.upper())

print(my_str.lower())


# print(".len() method of my_str is", my_str.len())
print("len(my_str) is", len(my_str))