lower=0
upper=0
s=input()
for i in s:
    if i==i.upper():
        upper+=1
    else:
        lower+=1
if upper<=lower:
    print(s.lower())
else:
    print(s.upper())