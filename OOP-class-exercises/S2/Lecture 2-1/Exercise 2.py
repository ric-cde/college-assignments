# The Fibonacci sequence is 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ... defined by beginning with two 1s and
# then adding the two previous numbers to get the nextone. Write a function fib(n) that returns
# a list of the first n Fibonacci numbers. For example, fib(5) → [1, 1, 2, 3, 5

def fib(n):
    sequence = []
    for i in range(1, int(n)+1):
        if i <= 2:
            sequence.append(1)
        else:
            sequence.append(sequence[-1] + sequence[-2])
    return sequence

numInput = input("How many Fibonacci numbers do you want? ")

print(fib(numInput))