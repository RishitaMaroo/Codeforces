n=int(input())
c=0
l=list(map(int,input().split(' ')))
mi=l[0]
ma=l[0]
for i in range(1,n):
    if l[i]>ma:
        ma=l[i]
        c=c+1
    elif l[i]<mi:
        mi=l[i]
        c=c+1
print(c)
