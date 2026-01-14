# Write a FOR loop that will iterate from 0 to 20. For each iteration, it will
# check if the current number is even or odd, and report that to the screen (e.g. "1 is odd, 2 is even").

for i in range(1,21):
    if i % 2 == 0:
        print(i, "is even")
    if i % 2 != 0:
        print(i, "is odd")