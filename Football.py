a=input()
c=1
a1=False
for i in range(1,len(a)):
    if a[i]==a[i-1]:
        c=c+1
        if c==7:
            a1=True
    else:
        c=1

if a1==True:
    print("YES")
else:
    print("NO")

