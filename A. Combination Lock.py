n=int(input())
s1=input()
s2=input()
c=0
for i in range(0,n):
    c=c+min(abs(int(s1[i])-int(s2[i])),10-abs(int(s1[i])-int(s2[i])))
    # print(c)
print(c)



