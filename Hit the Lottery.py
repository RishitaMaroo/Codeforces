l=[100,20,10,5,1]
n=int(input())
a=0
for i in range(0,5):
    a=a+int(n/l[i])
    n=n%l[i]
print(a)
