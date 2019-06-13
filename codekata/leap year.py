s=int(input())
if(s%4==0 and s%100!=0):
  print('yes')
elif(s%100==0):
  print('no')
elif(s%400==0):
  print('yes') 
else:
  print('no')
