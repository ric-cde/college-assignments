notdigits = True

while (notdigits):
    characters = input("Enter a number: ")
    notdigits = False
    for c in characters:
        if c.isalpha():
            print("Not a digit")
            notdigits = True
            continue


print("success")
sum = 0
characters = int(characters)

while (characters >= 1):
    sum += characters % 10
    characters = characters // 10
    print(characters)

print(sum)



#sum = 0

#for c in characters:
#    if c.isdigit():
#        sum += int(c)
#        print(c)

#print("Digit count:", sum)


# v2

