n = int(input())
a = [input().strip() for _ in range(n)]

a = sorted(set(a), key = lambda x: (len(x), x))

for i in a:
    print(i)