a=input()
o=''
a=a.lower()
for i in range(0,len(a)):
    if a[i]=='a' or a[i]=='e' or a[i]=='o' or a[i]=='u' or a[i]=='i'  or a[i]=='y':
        continue
    else:
        o=o+'.'+a[i]
print(o) 

