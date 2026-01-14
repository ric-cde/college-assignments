# Exercise 4: Write a function that asks the user for a number and prints
# the sum of all numbers from 1 to the number they enter.10

def sum_numbers(number):
    num_sum = 0
    for i in range(1, number + 1):
        num_sum += i
    return num_sum

print(sum_numbers(int(input("Enter a number: "))))