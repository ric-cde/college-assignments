# Write a Python function that takes a list of words and counts how many of them begin with ‘a’

def count_a(word_list):
    sum = 0
    for i in word_list:
        print(i)
        if i[0] == 'a':
            sum += 1
    return sum

my_list = input("Enter a list of words").split()

print(count_a(my_list))
