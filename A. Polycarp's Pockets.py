n=int(input())
l=list(map(int,input().split(' ')))
m=[]
for i in range(0,len(l)):
    p=l.count(l[i])
    m.append(p)
if len(l)==1:
    print(1)
else:
    print(max(m))