counter = 0
num = int(input("Enter a number: "))
min = num

while num >= 0:
    counter += 1
    num = int(input("Enter a number: "))
    if num < 0:
        break
    if num < min:
        min = num

print("Count is:", counter)
print("Smallest is:", min)



