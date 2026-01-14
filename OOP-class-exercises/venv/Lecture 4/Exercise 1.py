
counter = 0;

for c in range(2000,3200):
    if (c % 7 == 0) and (c % 5 != 0):
        counter += 1
        print(c)

print ("Count is", counter)