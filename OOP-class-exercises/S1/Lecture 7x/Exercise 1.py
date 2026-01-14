# Exercise 1: Write a function that takes a number as a parameter and prints the numbers from 1 to that number on the screen.


def num_counter(number):
    for i in range(1, number + 1):
        print(i)

num_counter(int(input("Enter a number")))
