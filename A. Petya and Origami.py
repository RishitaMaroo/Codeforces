a,b=map(int,input().split(' '))
u=a*2
v=a*5
w=a*8
s=0
r=0
t=0
# print(u,v,w)
if u%b==0:
    s=s+(u//b)
else:
    s=s+(u//b)+1
if v%b==0:
    r=r+(v//b)
else:
    r=r+(v//b)+1

if w%b==0:
    t=t+(w//b)
else:
    t=t+(w//b)+1
print(s+r+t)
