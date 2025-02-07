m=int(input("Enter the number of test cases: "))
for i in range (m):
  s=input("Enter the string: ")
  n=len(s)
  for i in range (0,n,2):
      print(s[i],end='')
  print(end=' ')
  for i in range (1,n,2):
      print(s[i],end='')
  print()
