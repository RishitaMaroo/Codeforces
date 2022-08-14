inp=int(input())
for i in range(0,inp):
    l=list(map(int,input().split()))
    l1=sorted(l)

    if l1[0]==l1[1] and l1[0]==l1[2]:
        print("YES")
        print(l1[0],l1[2],l1[2])
    elif l1[1]==l1[2]:
        print("YES")
        print(l1[0],l1[0],l1[2])
    else:
        print("NO")