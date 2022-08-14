inp=int(input())
for i in range(0,inp):
    x,y=map(int,input().split())
    if x==y:
        print(0)
        continue
    elif (y>x):
        if (x-y)%2!=0:
            print(1)
        else:
            print(2)
            continue
    else:
        if (x-y)%2!=0:
            print(2)
        else:
            print(1)
            continue
