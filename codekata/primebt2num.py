s,u=map(int,input().split())
for v in range(s+1,u):
  if v>1:
    for l in range(2,v):
      if(v%l==0):
        break
    else:
      print(v,end=' ')
