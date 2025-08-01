M = int(input())
N = int(input())
total = 0
num_min = N
for i in range(M, N+1):
    for j in range(2, i+1):
        if i % j == 0:
            if i == j:
                total += i
                num_min = min(i, num_min)
            break
if total:
    print(total)
    print(num_min)
else:
    print(-1)