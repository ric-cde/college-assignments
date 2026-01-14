# 2. Write a program that counts how many times the string 'hi' is contained in another string.
# For example for the string 'hi there, the sky is high, but the moon is higher' it should print 3.
import find

your_string = input("Enter a phrase: ")
substring = input("What sub-string to search for?")

counter = 0
start = 0

while start != -1:
    print(your_string.find(substring, start))
    # Check if substring is in string starting from start index
    start = your_string.find(substring, start)
    # If no, returns -1 and breaks loop
    # If yes, add one to counter and shift start index by + 1.
    if start != -1:
        counter += 1
        start += 1

print(substring, "found", counter, "times")