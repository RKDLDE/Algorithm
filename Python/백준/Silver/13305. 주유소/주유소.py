N = int(input())
km = list(map(int, input().split()))
price = list(map(int, input().split()))

min_price = price[0]
total_price = 0

for i in range(N - 1):
    total_price += km[i] * min_price
    min_price = min(min_price, price[i+1])
    
print(total_price)
