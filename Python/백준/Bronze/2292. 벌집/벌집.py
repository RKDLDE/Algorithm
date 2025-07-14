n = int(input())

floor = 1
end = 1

while n > end:
    end += floor * 6
    floor += 1

print(floor)