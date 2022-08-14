n=int(input())
for i in range(0,n):
    l=list(map(int,input().split(' ')))
    z=max((l[3]-l[0]),0)+max((l[4]-l[1]),0)
    if z<=l[2]:
        print("YES")   
    else:
        print("NO")
