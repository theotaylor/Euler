def reverse(word):
  x = 1
  new_word = ""
  for i in range(0,len(word)):
    new_word = new_word + word[len(word) - x]
    x += 1
  return new_word 
