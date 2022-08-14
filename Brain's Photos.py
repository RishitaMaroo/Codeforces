x,y=map(int,input().split())
l=[]
for i in range(x):  
    single_row = list(map(str,input().split()))  
    l.append(single_row)  
# printing the matrix given by user  
# print(l)  
v=False
for i in range(0,len(l)):
    for j in range(0,len(l[i])):
        # print(l[i][j])
        if l[i][j]=='C' or l[i][j]=="M" or l[i][j]=="Y":
            v=True          
if v==True:
    print("#Color")           
else:
    print("#Black&White")
    
