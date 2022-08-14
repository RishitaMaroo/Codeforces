a=0
b=0
for _ in range(int(input())):
    x,y=map(int, input().split())
    if x==y:
        a=a+0
        b=b+0
    elif x>y:
        a=a+1
    else:
        b=b+1
# print(a,b)
if a==b:
    print("Friendship is magic!^^")
elif a>b:
    print("Mishka")
else:
    print("Chris")