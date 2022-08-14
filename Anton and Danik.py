x=0
y=0
n=int(input())
a=input()
for i in range(0,n):
    if a[i]=='A':
        x=x+1
    else:
        y=y+1
if x>y:
    print("Anton")
elif y>x:
    print("Danik")
else:
    print("Friendship")