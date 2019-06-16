e= input()
k=0
for i in range(len(e)):
  if(e[i].isdigit() or e[i].isalpha() or e[i]==""):
    continue
  else:
    k=k+1
print(k)
