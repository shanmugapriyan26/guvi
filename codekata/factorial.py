u=int(input())
factorial=1
if(u>0):
  for a in range(1,u+1):
    factorial=factorial*a
  print(factorial)
elif(u==0):
  print('1')
