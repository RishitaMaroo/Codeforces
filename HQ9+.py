a=input()
flag=0
for i in a:
    if i=='H' or i=='Q' or i=='9':
        flag=1
if flag==1:
    print("YES")
else:
    print("NO")       