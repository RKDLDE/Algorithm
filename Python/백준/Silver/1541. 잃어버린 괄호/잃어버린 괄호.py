expression = input().split('-')

first = sum(map(int, expression[0].split('+'))) if expression[0] else 0
rest = sum(sum(map(int, part.split('+'))) for part in expression[1:])

print(first - rest)