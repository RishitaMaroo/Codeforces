n=input()
counter=False
while counter==False:
    n=int(n)+1
    n=str(n)
    if len(set(n))==4:
        counter=True
        print(n)
        break
