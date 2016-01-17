while True:
  x = 100
  y = 100
  final = 0
  for x in range(100,999):
    for y in range(100,999):
      num = x * y

      e = num % 10
      d = num % 100
      r = num % 1000
      t = num % 10000

      stringnum = str(num)

      while len(stringnum) == 5:
        if int(stringnum[0]) == e and int(stringnum[1]) == (d - e) / 10:
          final = num

      while len(stringnum) == 6:
        if int(stringnum[0]) == e and int(stringnum[1]) == (d - e) / 10 and int(stringnum[2]) == (r - d) / 1000:
          final = num

      print final
