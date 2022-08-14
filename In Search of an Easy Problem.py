c=0
a=int(input())
l=list(map(int,input().split(' ')))
for i in l:
    if i==1:
        c=c+1
    
if c==0:
    print("EASY")
else:
    print("HARD")        