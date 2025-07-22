N = int(input())
p_list = sorted(list(map(int, input().split())))
sum = 0

for i in range(0, N):
    sum += p_list[i] * (N-i)
print(sum)