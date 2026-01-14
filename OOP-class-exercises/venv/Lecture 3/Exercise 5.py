#Write a program that asks the user for a number and printsthe sum of all numbers from 1 to the number they enter.

i = int(input("Enter a number "))
j = 0
sum = 0


while j <= i:
    sum += j
    print("Adding sum +", j, "=", sum)
    j += 1

print("Sum is", sum)

sum = 0
for j in range(1,(i+1)):
    sum += j
    print(j)
print(sum)