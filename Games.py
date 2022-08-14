n=int(input())
l=[]
m=[]
c=0
for i in range(0,n):
    x,y=list(map(int,input().split(' ')))
    l.append(x)
    m.append(y)

for i in range(0,n):
    for j in range(0,n):
        if l[i]==m[j]:
            c=c+1
print(c)
