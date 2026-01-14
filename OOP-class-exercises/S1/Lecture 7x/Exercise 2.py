# Exercise 2: Write a function that takes a number as a parameter and iterates from 0 to that number.
# For each iteration, it will check if the current number is even or odd, and report that to the screen (e.g. "1 is odd, 2 is even")

def num_counter(number):
    for i in range(1, number + 1):
        if i % 2 == 0:
            print(i, "is even")
        if i % 2 > 0:
            print(i, "is odd")

num_counter(int(input("Enter a number")))
