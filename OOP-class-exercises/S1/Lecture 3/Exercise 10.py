# Write a program that uses loops to print the triangle below
n = 5
l = n-1

for i in range(0,n):
    for k in range(0,l):
        print(" ", end="")
    for j in range(0,(i+1)):
        print("*", end ="")
    for j in range(0, (i+1)):
        print("*", end=""),
    for k in range(0, l):
        print(" ", end="")
    l -= 1
    print("")