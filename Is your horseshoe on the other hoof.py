k=[]
l=list(map(int,input().split(' ')))
for i in range(0,len(l)):
    if l[i] not in k:
        k.append(l[i])
print(len(l)-len(k))