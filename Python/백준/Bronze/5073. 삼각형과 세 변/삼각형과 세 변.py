while True:
    command = input()
    if command.strip() == "0 0 0":
        break

    t = sorted(list(map(int, command.split())), reverse = True)
    if t[0] == t[1] == t[2]:
        print("Equilateral")
    elif t[0] >= t[1] + t[2]:
        print("Invalid")
    elif t[0] == t[1] or t[0] == t[2] or t[1] == t[2]:
        print("Isosceles")
    else:
        print("Scalene")