n = int(input())
x_c = []
y_c = []

for _ in range(n):
    x, y = map(int, input().split())
    x_c.append(x)
    y_c.append(y)

print((max(x_c)-min(x_c)) * (max(y_c)-min(y_c)))