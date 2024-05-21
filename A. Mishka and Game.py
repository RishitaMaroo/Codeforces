a1=0
a2=0
n=int(input())
for i in range(0,n):
    a,b=map(int,input().split())
    if a>b:
        a1+=1
    elif a<b:
        a2+=1
if a1>a2:
    print("Mishka")
elif a1<a2:
    print("Chris")
else:
    print("Friendship is magic!^^")