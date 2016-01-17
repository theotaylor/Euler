
def reverse(word):
  x = 1 
  new_word = ""
  for i in range(0,len(word)):
    new_word = new_word + word[len(word) - x]
    x += 1
  return new_word 



x = 100
y = 100
final = 0
for x in range(100,999):
  for y in range(100,999):
    num = x * y
    stringnum = str(num)
    if stringnum == reverse(stringnum) and  num > final:
        final = num
print final  

