# Write a Python function to replace every word in a sentence which is longer than 6 characters with “blah”.
# Use the function to read a text from a file, replace every long word with ‘blah and write the output in another file.

def blah_fix(sentence):
    sentence = sentence.replace(",", " ,").replace(".", " .").split()
    counter = 0
    for w in sentence:
        if (len(w) > 6):
            sentence[counter] = 'blah'
        counter += 1
    return ' '.join(sentence).replace(" ,", ",").replace(" .", ".")

f = open('twinkle.txt', 'r')
o = open('out.txt', 'w')
for line in f.readlines():
    o.write(blah_fix(line)+'\n')
f.close()
o.close()