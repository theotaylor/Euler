while True:
  x = 100
  y = 100
  for x in range(100,999):
    for y in range(100,999):
      revnum = x * y
      num = x * y
      revnum = str(revnum)
      num = str(num)
      if len(revnum) == 5:

         revnum[0] = num[4] 
         revnum[4] = num[0]
         revnum[1] = num[3] 
         revnum[3] = num[1]
         revnum = int(revnum)
         num = int(num)

      if revnum == num:
        a = num

      if len(revnum) == 6:

        revnum[0] = num[5]
        revnum[5] = num[0]
        revnum[1] = num[4]
        revnum[4] = num[1]
        revnum[2] = num[3]
        revnum[3] = num[2]
        revnum = int(revnum)
        num = int(num)

      if revnum == num:
        a = num 
      
      if y == 999:
         print a
        
