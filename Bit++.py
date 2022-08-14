a=int(input())
b=0
for i in range(0,a):
    s=input()
    if s=='X++':
        b=b+1
    elif s=='++X':
        b=b+1
    elif s=='--X':
        b=b-1
    elif s=='X--':
        b=b-1
print(b)
        
