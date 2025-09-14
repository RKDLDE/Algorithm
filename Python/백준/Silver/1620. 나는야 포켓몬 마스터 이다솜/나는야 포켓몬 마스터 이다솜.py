import sys
input = sys.stdin.readline
n, m = map(int, input().split())

names = [input().strip() for _ in range(n)]
numbers = {name : i + 1 for i, name in enumerate(names)}

for _ in range(m):
    a = input().strip()
    
    if a.isdigit():
        print(names[int(a) - 1])
    else:
        print(numbers[a])