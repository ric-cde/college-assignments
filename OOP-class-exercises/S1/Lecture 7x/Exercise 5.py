# Exercise 5: Write a function to print a factorial of a number.

def sum_numbers(number):
    num_mult = 1
    for i in range(number, 0, -1):
        print(i)
        num_mult *= i;
    return num_mult

print(sum_numbers(int(input("Enter a number: "))))