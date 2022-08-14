c=0
a=int(input())
for i in range(0,a):
    x,y=map(int,input().split(' '))
    if y-x>=2:
        c=c+1
print(c)