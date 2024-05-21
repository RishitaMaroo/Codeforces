n=int(input())
a='codeforces'
for i in range(0,n):
    c=0
    s=input()
    for i in range(0,len(s)):
        if s[i]!=a[i]:
            c+=1
    print(c)
            