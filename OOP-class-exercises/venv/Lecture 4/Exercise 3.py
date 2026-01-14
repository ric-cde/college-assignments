string = input("Enter a string: ")
alphacounter = 0
digitcounter = 0

for c in string:
    if c.isdigit():
        digitcounter += 1
        print (c)
    elif c.isalpha():
        alphacounter += 1
        print (c)


print("Digit count:", digitcounter)
print("Alpha count:", alphacounter)