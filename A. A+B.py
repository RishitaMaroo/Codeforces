n=int(input())
for i in range(0,n):
    s=input()
    if "+" in s:
        l=s.split('+')
    print(int(l[0])+int(l[1]))