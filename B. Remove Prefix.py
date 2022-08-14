for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
 
    t = set()
    i = n - 1
    while i >= 0 and a[i] not in t:
        t.add(a[i])
        i -= 1
    print(i+1)
 