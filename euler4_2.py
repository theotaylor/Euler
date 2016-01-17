while True:
  x = 100
  y = 100
  for x in range(100,999):
    for y in range(100,999):
      #revnum = x * y
      num = x * y

      e = num % 10
      d = num % 100
      r = num % 1000
      t = num % 10000

        #str(num) = stringnum

      while len(str(num)) == 5:
        if str(num[0]) == str(e) and str(num[1]) == str((d - e) / 10):
          final = num

      #while len(num) == 5:
        #if int(stringnum[0]) = e and int(stringnum[1]) = (d - e) / 10
          #final = num 

      while len(str(num)) == 6:
        if str(num[0]) == str(e) and str(num[1]) == ((d - e) / 10) and str(num[2]) == ((r - d) / 1000):
          final = num

      #while len(num) == 6:
        #if int(stringnum[0]) = e and int(stringnum[1]) = (d - e) / 10 and int(stringnum[2] = (r - d) / 1000:

      print final
