
for _ in range(0,int(input())):
    a=1
    l=list(map(int,input().split()))
    if l[2]==1:
        print("YES")
        continue
    while(l[0]%2==0):
        a=a*2
        # print(a)
        l[0]=l[0]/2
        # print(l[0])
    while(l[1]%2==0):
        a=a*2
        l[1]=l[1]/2
    if l[2]<=a:
        print("YES")
    else:
        print("NO")