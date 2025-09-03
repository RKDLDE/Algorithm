n = input()
a = []
for i in n:
    a.append(i)
print(int(''.join(sorted(a, reverse = True))))