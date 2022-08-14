c=0
d=0
a=input()
for i in a:
    if i==i.upper():
        c=c+1
    else:
        d=d+1
if c>d:
    print(a.upper())
else:
    print(a.lower())