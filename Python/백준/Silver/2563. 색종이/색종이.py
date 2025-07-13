array = [[0 for col in range(100)] for row in range(100)]

N = int(input())

for _ in range(N):
    x, y = map(int, input().split())
    for x2 in range(x, x+10):
        for y2 in range(y, y+10):
            array[x2][y2]=1

print(sum(sum(row) for row in array))