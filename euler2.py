
x = 0
y = 1
total = 0

while x or y <= 4000000:
  x = y + x
  if x % 2 == 0:
    total += x
  y = y + x
  if y % 2 == 0:
    total += y
print total
