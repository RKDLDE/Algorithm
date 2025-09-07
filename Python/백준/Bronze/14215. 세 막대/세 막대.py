t = sorted(list(map(int, input().split())), reverse = True)
if t[0] >= t[1] + t[2]:
    t[0] = t[1] + t[2] - 1
print(sum(t))