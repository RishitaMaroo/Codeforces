n=int(input())
for i in range(0,n):
    sum=0
    p=[]
    a=int(input())
    l=list(map(int,input().split(' ')))
    for i in range(0,len(l)-1):
        sum=sum+l[i]
        if sum%l[-1]==0 or l[-1]%sum==0:
            p.append(1)
        else:
            p.append(0)
    if len(set(p))==1:
        print("YES")
    else:
        print("NO")