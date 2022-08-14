x,y,z=map(int,input().split(' '))
if x%z == 0:
    k = 0
else:
    k = 1
if y%z == 0:
    p = 0
else:
    p = 1
temp = (x//z)+k
temp1 = (y//z)+p
print(temp*temp1)