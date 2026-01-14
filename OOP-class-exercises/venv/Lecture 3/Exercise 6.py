# Write a program to calculate and print the factorial of a number using a FORloop.
# #The factorial of a number is the product of all integers up to and including that number,
# #so the factorial of 4 is 4*3*2*1= 24

num = int(input("Enter a number "))
sum = 1
j = 1

while j <= num:
    print(j)
    sum *= j
    j += 1

print(sum)

sum = 1
for i in range(1,(num+1)):
    sum *= i

print(sum)