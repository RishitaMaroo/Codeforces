n=int(input())
for i in range(0,n):
    a=int(input())
    if a%2==0:
        print(int((a/2)-1))
    else:
        print(int(a//2))
