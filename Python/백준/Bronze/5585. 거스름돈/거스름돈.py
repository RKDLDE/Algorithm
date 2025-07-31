N = 1000 - int(input())
coins = [500, 100, 50, 10, 5, 1]

count = 0
for i in coins:
    count += N // i
    N %= i

print(count)