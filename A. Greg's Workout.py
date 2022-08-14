n=int(input())
a=[]
b=[]
c=[]
l=list(map(int,input().split()))
for i in range(0,len(l)):
    if i%3==0:
        a.append(l[i])
    elif i%3==1:
        b.append(l[i])
    else:
        c.append(l[i])
if sum(a)>sum(b) and sum(a)>sum(c):
    print("chest")
elif sum(b)>sum(a) and sum(b)>sum(c):
    print("biceps")
elif sum(c)>sum(a) and sum(c)>sum(b):
    print("back")
