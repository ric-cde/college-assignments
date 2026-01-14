# Exercise 3: Write a function that takes a number as a parameter, iterates from 0 to that number,
# and for each iteration of the loop,
# multiplies the current number by 9 and prints the result (e.g. "2 * 9 = 18").

def num_counter(number):
    for i in range(1, number + 1):
        print(i, "* 9 =", result_multiply(i))

def result_multiply(number):
    return number * 9

num_counter(int(input("Enter a number: ")))
