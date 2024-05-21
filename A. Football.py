from collections import Counter
l=[]
n=int(input())
for i in range(0,n):
    s=input()
    l.append(s)
d=Counter(l)
max_key = max(d, key=d.get)
print(max_key)
