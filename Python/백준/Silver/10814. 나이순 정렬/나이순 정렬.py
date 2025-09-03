n = int(input())
a = [input().split() for _ in range(n)]

for age, name in sorted(a, key = lambda x: int(x[0])):
    print(age, name)