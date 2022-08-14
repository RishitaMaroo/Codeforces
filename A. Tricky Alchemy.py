yc,bc=map(int,input().split(" "))
y,g,b=map(int,input().split(" "))
nyc=y*2+g
# print(nyc)
nbc=b*3+g
# print(nbc)
print(max(0,nyc-yc)+max(0,nbc-bc))
