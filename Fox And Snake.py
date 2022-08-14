x,y=map(int,input().split(' '))
a="."*(y-1)
b="#"
c="#"*y
for i in range(x):
    if i%2==0:
        print(c)
    else:
        print("{}{}".format(a,b))
        a,b=b,a
