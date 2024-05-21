n=int(input())
for i in range(n):
    counter=0
    a,b,c,d=map(int,input().split())
    if a<b:
        counter+=1
    if a<c:
        counter+=1
    if a<d:
        counter+=1    
    print(counter)
    