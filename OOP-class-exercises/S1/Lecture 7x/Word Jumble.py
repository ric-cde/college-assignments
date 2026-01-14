word = 'abracadabra'
i = 3
j = 4
def letter_swap(word,i,j):
  if (i>=j):
    return False
  return word[:i] + word[j] + word[i+1:j] + word[i] + word[j+1:]

print(letter_swap(word))