n = int(input())
cards = set(map(int, input().split()))

m = int(input())
iscards = list(map(int, input().split()))

print(' '.join(['1' if i in cards else '0' for i in iscards]))