n=input()
c=0
for i in n:
    if i=='H' or i=='Q' or i=='9':
        c=1
    
if c==0:
    print("NO")
else:
    print("YES")