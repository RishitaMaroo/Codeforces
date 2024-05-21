s=0
a,b,c=map(int,input().split())
for i in range(1,c+1):
    s=s+i*a
if (s)>b:
    print(s-b)
else:
    print(0)