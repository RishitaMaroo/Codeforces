a=int(input())
s=input()
Anton=s.count("A")
Danik=s.count("D")
if Anton==Danik:
    print("Friendship")
elif Anton > Danik:
    print("Anton")
else:
    print("Danik")
    