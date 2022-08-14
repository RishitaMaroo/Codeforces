inp=int(input())
row,col=(inp,inp)
a=[[0]*col]*row
a[0][0]=1

for i in range(0,row):
    for j in range(0,col):
        a[i][j]=a[i-1][j]+a[i][j-1]
        print(a[i][j])


# for i in range(1,inp+1):
#     for j in range(1,inp+1):
#         if i==1:
#             a[i][j]=1
#         elif j==1:
#             a[i][j]=1 
#         else:
#             a[i][j]=a[i-1][j]+a[i][j-1]
#     print(a[i][j])      
