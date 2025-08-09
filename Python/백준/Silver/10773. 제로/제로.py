n = int(input())
money = []

for _ in range(n):
    input_money = int(input())

    if money and input_money == 0:
        money.pop(-1)
    else:
        money.append(input_money)

print(sum(money))