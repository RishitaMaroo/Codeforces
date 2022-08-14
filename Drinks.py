c=0
a=int(input())
l=list(map(int,input().split(' ')))
for i in l:
    c=c+i/100
print((c/a)*100)
