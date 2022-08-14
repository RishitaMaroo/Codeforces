for _ in range(int(input())):
    input()
    s = input().split()
    print(s.index(min(s, key=s.count)) + 1)