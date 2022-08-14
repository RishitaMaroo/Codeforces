for _ in range(int(input())):
    n,h,m=map(int,input().split())
    x=h*60+m
    a=[]
    for i in range(n):
        h,m=map(int,input().split())
        a.append((h*60+m-x)%(24*60))
    ans=sorted(a)[0]
    print(ans//60,ans%60)
