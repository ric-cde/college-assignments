num = int(input("Enter a number: "))

counter = 1

while (counter <= num):
    if (num % counter == 0):
        print(counter)
    counter += 1