a=int(input())
b=0
for i in range(0,a):
    x,y,z=[int(x) for x in input().split()]
    if  (x==1 and y==1) or (y==1 and z==1) or (x==1 and z==1):
        b=b+1    
print(b) 