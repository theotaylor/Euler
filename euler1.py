def euler1():
  x = 1 
  for i in range(1000):
    if i % 3 and i % 5: 
      x += i
    elif i % 3:
      x += i
    elif i % 5:
      x += i
    print x  
  return x
      
           
