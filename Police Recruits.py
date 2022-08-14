n= int(input())
list1 = list(map(int, input().split(' ')))
cou = 0
ans = 0
for i in list1:
    if i == -1:
        if cou > 0:
            cou -= 1
        else:
            ans += 1
    else:
        cou += i
print(ans)