n = int(input())
a = list(map(int, input().split()))
b = sorted(set(a))

rank = {value: idx for idx, value in enumerate(b)}

for i in a:
    print(rank[i], end=' ')