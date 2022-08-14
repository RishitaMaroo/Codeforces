n=int(input())
for i in range(0,n):
    t=int(input())
    l=list(map(int,input().split(" ")))
    c=0
    if all(l[i]%2==l[i+2]%2 for i in range(t-2)):
        print("YES")
    else:
        print("NO")

    
    
