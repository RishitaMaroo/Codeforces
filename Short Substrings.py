n=int(input())
for i in range(0,n):
    s=input()
    a=''
    a+=s[0]
    for j in range(1,len(s)-1,2):
        a=a+(s[j])
    a=a+(s[len(s)-1])
    print(a)