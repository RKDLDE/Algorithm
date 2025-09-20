import sys
input = sys.stdin.readline

n, m = map(int, input().split())

a = set([input().strip() for _ in range(n)])
b = set([input().strip() for _ in range(m)])
c = a & b

print(len(c))
print('\n'.join(sorted(c)))