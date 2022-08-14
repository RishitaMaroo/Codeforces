a=int(input())
b=list(map(int,input().split(' ')))
c=list(map(int,input().split(' ')))
d=[]
m=0

#adding the no. of levels to the list d
for i in range(1,b[0]+1):
	d.append(b[i])
for i in range(1,c[0]+1):
	d.append(c[i])


#checking if all levels are in list or not
for i in range(1,a+1):
	if (not(i in d)):
		m=1
		print ("Oh, my keyboard!")
		break

if (m==0):
	print ("I become the guy.")