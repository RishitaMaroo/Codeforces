a=int(input())
z=str(a).count('4')
y=str(a).count('7')
#print(z,y)
b=z+y
if a==4 or a==7:
    print("NO")
elif b==4 or b==7:
    print("YES") 
else:
    print("NO")