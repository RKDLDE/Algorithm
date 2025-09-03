a = []
for _ in range(5):
    a.append(int(input()))

print(int(sum(a)/len(a)))
print(sorted(a)[2])