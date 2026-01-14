import random

secret = random.randrange(0,2000)
guess = False

while (guess != secret):
    guess = int(input("Guess the number: "))
    if guess > secret:
        print("Lower!")
    elif guess < secret:
        print("Higher!")
    elif guess == secret:
        print("You guessed correctly - it's", secret)



