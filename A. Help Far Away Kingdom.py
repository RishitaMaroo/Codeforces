s=input()
a=s.split('.')
if a[0][-1]=='9':
    # print(a[0][-1])
    print("GOTO Vasilisa.")
else:
    # print(a[1][0])
    if int(a[1][0]) > 4:
        print(int(a[0])+1)
    else:
        print(int(a[0]))