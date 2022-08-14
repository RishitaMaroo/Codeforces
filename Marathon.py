n=int(input())
for i in range(0,n):
    sum=0
    l=list(map(int,input().split(' ')))
    if l[0]<l[1]:
        sum=sum+1
    if l[0]<l[2]:
        sum=sum+1
    if l[0]<l[3]:
        sum=sum+1
    print(sum)


