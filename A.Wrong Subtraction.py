a, b =map(int,input().split())
for i in range(0,b):
    if a%10!=0:
        a=a-1
    else:
        a=a//10
print(a)

