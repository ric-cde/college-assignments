# Exercise 6: Write a function that takes a string as a parameter and returns a sting
# that is made up of the first two characters and the last two characters.
# If the string has a length less than 4 the program prints a message on the screen.


def jumbotron(myStr):
    if len(myStr) <= 4:
        print("Error! Too short.")
    else:
        return myStr[:2] + myStr[-2:]

print(jumbotron(input("Enter a string of over 4 chars to be clipped: ")))