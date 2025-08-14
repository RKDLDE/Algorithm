n = int(input())
for _ in range(n):
    ps = input()
    stack = 0

    for i in ps:
        if i == "(":
            stack += 1
        else:
            stack -= 1

        if stack < 0:
            stack = -1
            break

    print("YES") if stack == 0 else print("NO")