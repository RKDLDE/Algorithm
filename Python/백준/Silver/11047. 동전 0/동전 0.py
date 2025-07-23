N, K = map(int, input().split())

coins = sorted([int(input()) for _ in range(N)], reverse = True)
cnt = 0
while K > 0:
    for i in coins:
        if K >= i:
            cnt += K//i
            K %= i
print(cnt)