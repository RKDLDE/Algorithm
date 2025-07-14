n = int(input())
arr = [25, 10, 5, 1]
for _ in range(n):
    d = int(input())
    for i in arr:
        print(d//i, end = ' ')
        d %= i