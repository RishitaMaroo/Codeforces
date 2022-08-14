sum=0
x,y,z=map(int,input().split(" "))
for i in range(1,z+1):
    sum=sum+x*i
if sum>y:
    print(sum-y)
else:
    print(0)
