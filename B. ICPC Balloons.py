a=int(input())
for i in range(0,a):
    t=int(input())
    s=input()
    counts_dict = {}
    for c in list(s):
        if c not in counts_dict:
            counts_dict[c] = 0
        counts_dict[c] += 1
    sum=0
    for key, value in counts_dict.items():
        
        # print(value)
        if value==1:
            sum=sum+2
        if value>1:
            sum=sum+(value-1)+2
    print(sum)

