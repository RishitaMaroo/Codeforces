a,b=map(int,input().split())
count=1
while True:
    a=a*3
    b=b*2
    if a>b:
        break
    count+=1
print(count)