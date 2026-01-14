# Write a Python function that takes a list of words and a character,
# and counts how many of the words in the list begin with that character

def count_a(word_list, my_char):
    sum = 0
    for i in word_list:
        print(i)
        if i[0] == my_char:
            sum += 1
    return sum

my_list = input("Enter a list of words: ").split()
my_char = input("Enter a character to count among first letters: ")

print(count_a(my_list, my_char))
