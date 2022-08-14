a=['a','e','i','o','u','y']
s=input().lower()
if s[-2]==" ":
    s=s.replace(" ",'')
    # print(s)
if s[-2] in a:
    print("YES")
else:
    print("NO")

