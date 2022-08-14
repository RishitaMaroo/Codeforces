a=int(input())
l=[]
c=0
for i in range(1,a+1):
    p=input()
    l.append(p)
    if l[i-1]!=l[i-2]:
        c=c+1
print(c+1)

