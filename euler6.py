def adding(num):
  i = num
  while i > 0:
    i -= 1
    num += i
  return num

def adding_squares(num):
  total = 0
  for i in range(1,num+1):
    total = i * i + total
  return total

x = 100
print adding(x) **2 - adding_squares(x) 

