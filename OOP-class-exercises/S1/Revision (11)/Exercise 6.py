# Write a Python program that reads text from a file and generates a dictionary – a list of unique words.
# Save those words in a new file, one word per line

f = open('twinkle.txt', 'r')
o = open('out.txt', 'w')
dictionary = f.read().split()
for w in dictionary:
    o.write(w+'\n')
print(dictionary)