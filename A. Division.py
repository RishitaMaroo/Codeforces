n=int(input())
for i in range(0,n):
    a=int(input())
    if 1900<= a:
        print("Division 1")
    elif 1600<= a <=1899:
        print("Division 2")
    elif  1400 <= a <=1599:
        print("Division 3")
    else:
        print("Division 4")