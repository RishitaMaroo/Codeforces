for i in range(0,int(input())):
    n=input()
    if len(n)%2==0:
        if n[0:(len(n)//2)]==n[(len(n)//2):]:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")