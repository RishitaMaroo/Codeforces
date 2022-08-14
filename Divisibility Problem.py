n=int(input())
l=[]
for i in range(0,n):
    x,y=map(int,input().split(' '))
    if x%y==0:
        l.append(0)
    else:
        l.append(y-(x%y))
for i in l:
    print(i)