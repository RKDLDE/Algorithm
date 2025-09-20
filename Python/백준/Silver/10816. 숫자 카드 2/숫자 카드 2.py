import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

count_a = Counter(a)
print(' '.join(str(count_a[x]) for x in b))