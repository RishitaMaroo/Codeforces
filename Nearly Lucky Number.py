c=0
a=0
n=int(input())
for i in str(n):
    if i=='4' or i=='7':
        c=c+1
for i in str(c):
    if i=='4' or i=='7':
        a=a+1
if a==1:
    print("YES")
else:
    print("NO")
