  num = 100
  x = 0
  y = 0
  for i in range(100):
    x += num^2
    num -= 1
    y += num
    num -= 1
    y = y^2
  total = x - y 
  print total 
