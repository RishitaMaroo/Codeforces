
for i in range(0,int(input())):
    a=1
    s=input()
    for j in range(0,len(s)+1):
        if s[j]!=s[j-1] and s[j]!=s[j+1]:
            a=0
    if a==1:
        print("YES")
    else:
        print("NO")