c=0
x,y=map(int,input().split(' '))
l=list(map(int,input().split(' ')))
for i in range(0,x):
    if l[i]>y:
        c=c+2
    else:
        c=c+1
print(c)