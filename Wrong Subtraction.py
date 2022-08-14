x,y=map(int,input().split(' '))
for i in range(0,y):
    if x%10==0:
        x=x/10
    else:
        x=x-1
print(int(x))