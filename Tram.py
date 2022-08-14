a=int(input())
s=0
c=0
for i in range(0,a):
    x,y=map(int,input().split(' '))
    s=s-x
    s=s+y
    if s>c:
        c=s
print(c)