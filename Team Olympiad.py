inp=int(input())
l=list(map(int,input().split(' ')))
a=l.count(1)
b=l.count(2)
c=l.count(3)
z=min(a,b,c)
print(z)
res = []
e=[]
f=[]
g=[]
for i in range(0,len(l)):
    if l[i]==1:
        e.append(i+1)
        
    elif l[i]==2:
        f.append(i+1)
    else:
        g.append(i+1)

for i in range(0,z):
    print(e[i],f[i],g[i])



# for i in range(0,len(l)):

    