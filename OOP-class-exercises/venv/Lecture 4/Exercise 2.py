string = input("Enter a string: ")
counter = 0

for c in string:
    if c >= '0' and c <= '9':
    # if '0' <= c <= '9':
        counter += 1
        print (c)

print("Integer count:", counter)
