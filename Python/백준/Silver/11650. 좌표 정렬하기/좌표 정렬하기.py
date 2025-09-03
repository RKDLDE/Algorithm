n = int(input())
a = []
for _ in range(n):
    x, y = map(int, input().split())
    a.append([x, y])

for x, y in sorted(a, key = lambda a: [a[0], a[1]]):
    print(x, y)