a=input()
b=input()
c=input()
l=list(a)
m=list(b)
k=list(c)
l=l+m

if sorted(l)==sorted(k):
    print("YES")
else:
    print("NO")