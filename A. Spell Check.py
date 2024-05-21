t='Timur'
t=''.join(sorted(t))
n=int(input())
for i in range(0,n):
    a=int(input())
    s=input()
    s=''.join(sorted(s))
    if a==5:
        if  s==t:
            print("YES")
        else:
            print('NO')
    else:
        print("NO")  