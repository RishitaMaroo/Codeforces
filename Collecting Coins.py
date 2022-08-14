for _ in range(0,int(input())):
    l=list(map(int,input().split()))
    a=sum(l)
    if (a%3==0):
        av=a/3
        if (l[0] <= av and l[1] <= av and l[2] <= av):
            print("YES")
        else:
            print("NO")
    else:
         print("NO")
    