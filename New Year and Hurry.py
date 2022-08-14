x,y=map(int,input().split(" "))
c=0
a=0
for i in range(1,x+1):
    a=a+i*5
    if a+y<=240:
        c=c+1
print(c)
