R = lambda : list(map(int,input().split()))
n,a,b = R(),R(),R()
print(*(x for x in a if x in b))
