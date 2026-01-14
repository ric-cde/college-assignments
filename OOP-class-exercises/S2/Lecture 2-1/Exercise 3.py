# Write a Python program that will simulate “Guess the number” game.
# The computer thinks of a secret number between 1 and 100 (you can randomly generate that number).
# You are asked to enter your guess and the computer will print if the secret number is larger or smaller
# than the number you guessed. The game stops when you guess the number, or when you enter 0 to exit.

import random

secret = random.randint(1, 100)
print(secret)

print("I’m thinking of a secret number between 1 and 100. What is your guess? Enter 0 to exit.")
counter = 0

while True:
    guess = input()
    counter += 1
    if not guess.isdigit():
        print("Error! Must enter a number between 1 and 100")
    else:
        guess = int(guess)
        if guess == 0:
            print("Exiting...")
            break
        elif guess > 100 or guess < 1:
            print("Error! Must enter a number between 1 and 100")
        elif guess == secret:
            print("CORRECT")
            break
        elif guess > secret:
            print("You guessed too high")
        elif guess < secret:
            print("You guessed too low")
        if counter == 10:
            print("You've run out of guesses!")
            break


