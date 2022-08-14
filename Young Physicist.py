m=[]
s=0
a=0
b=0
for _ in range(0,int(input())):
    l=list(map(int,input().split()))
    m.append(l)
for i in range(0,len(m)):
    s=s+m[i][0]
    a=a+m[i][1]
    b=b+m[i][2]
if s==0 and a==0 and b==0:
    print("YES")
else:
    print("NO")