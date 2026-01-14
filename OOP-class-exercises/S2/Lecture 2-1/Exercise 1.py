# : Write a function divisors(n) that returns a list of the divisors of the integer n including 1 but excluding the
# number itself. For example, divisors (24) → [1,2,3,4,6,8,12]Write a small test program that asks the user for a number
# and prints the divisors of that number.

def divisors(n):
    n = int(n)
    outNum = []
    for i in range(1, n):
        if n % i == 0: # and i != n:
            outNum.append(i)
    return outNum

numInput = input("Enter a number: ")
print(divisors(numInput))