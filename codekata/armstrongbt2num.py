s,u=map(int,input().split())
for i in range(s+1,u):
  a=i
  b=0
  while(a!=0):
    s=a%10
    b=b+s**3
    a=a//10
  if(i==b):
    print(i,end=' ')
