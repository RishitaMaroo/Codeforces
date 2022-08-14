c=0
x,y=map(int,input().split(' '))
while(True):
    x=3*x
    y=2*y
    c=c+1
    if (x>y):
        break
print(c)
