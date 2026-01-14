# Write a Python function to replace every third word in a sentence with “hello”.
# Use the function to read a text from a file,
# replace every third word with ‘hello’ and
# write the output in another file.

# def rep(sentence):
#     list_str = sentence.split()
#     counter = 0
#     for w in list_str:
#         if ((counter + 1) % 3 == 0):
#             list_str[counter] = 'hello'
#         counter += 1
#     return list_str
#
#
# mySentence = "This is a sentence for checking whether the third word gets replaced"
# print(rep(mySentence))

def rep(in_text):
    counter = 0
    new_list = []
    for sentence in in_text:
        sentence = sentence.split()
        for w in sentence:
            if ((counter + 1) % 3 == 0):
                sentence[counter % len(sentence)] = 'hello'
            counter += 1
        sentence = ' '.join(sentence)
        new_list.append(sentence)
    new_list = '\n'.join(new_list)
    return new_list


f = open('twinkle.txt', 'r')
o = open('out.txt', 'w')
file_text = f.readlines()
o.write(rep(file_text))
f.close()
o.close()

