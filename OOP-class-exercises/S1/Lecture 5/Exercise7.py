# 1. Write a program that checks if a string is a valid password.

# A valid password should contain at least one lowercase letter,
# at least one uppercase letter, at least one special character from '+-%$!@'
# and be between 6 and 10 characters in length.

pw_correct = False

while (pw_correct == False):
    password = input("Enter a password: ")
    if (6 <= len(password) <= 10):
        upper = False
        lower = False
        special = False
        for c in password:
            if c.isupper():
                upper = True
            if c.islower():
                lower = True
            if c in ['+', '-', '%', '$', '!', '@']:
                special = True
                print("Special char detected")
        if (upper == True) and (lower == True) and (special == True):
            pw_correct = True
        else:
            print("Password must contain at least one uppercase, lower, and special character")
    else:
        print("Password must be between 6 & 10 characters")
print("Success! Password stored.")
