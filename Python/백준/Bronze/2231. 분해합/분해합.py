N = int(input())

for i in range(N):
    total = i + sum(int(j) for j in str(i))

    if total == N:
        print(i)
        break
else:
    print(0)