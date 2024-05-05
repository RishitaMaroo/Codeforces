n=int(input())
x=0
for i in range(0,n):
    a, b, c= map(int,input().split())
    if a+b+c>1:
        x+=1
print(x)
