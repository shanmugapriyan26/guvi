s=int(input())
u=list(map(int,input().split()))
u.sort()
med=u[int(s/2)]
print(med)
