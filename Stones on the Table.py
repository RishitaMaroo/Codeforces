c=0
a=int(input())
s=input()
for i in range(0,a-1):
    if s[i]==s[i+1]:
        c=c+1

print(c)