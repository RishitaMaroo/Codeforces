n=int(input())
steps=0
for i in range(n):
    a,b=map(int,input().split())
    if b-a>=2:
        steps+=1
print(steps)