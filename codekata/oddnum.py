s,u=map(int,input().split())
if(s<u):
  for i in range(s+1,u,1):
     if i%2!=0:
        print(i,end=' ')
