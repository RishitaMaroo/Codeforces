n=int(input())
for i in range(0,n):
    a,b,c=map(int,input().split())
    if a+b==c:
        print("+")
    else:
        print("-")