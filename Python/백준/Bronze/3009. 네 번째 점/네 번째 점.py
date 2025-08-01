xarr = []
yarr = []
for _ in range(3):
    x, y = map(int, input().split())
    xarr.append(x)
    yarr.append(y)

for x in xarr:
    if xarr.count(x) == 1:
        nx = x
for y in yarr:
    if yarr.count(y) == 1:
        ny = y

print(nx, ny)