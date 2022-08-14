n=int(input())
s=0
d={"Tetrahedron":4,"Cube":6,"Octahedron":8,"Dodecahedron":12,"Icosahedron":20}
for i in range(1,n+1):
    a=input()
    for j in d:
        if a==j:
            s=s+d[j]
print(s)