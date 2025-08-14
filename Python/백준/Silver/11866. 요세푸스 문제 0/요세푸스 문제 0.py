n, k = map(int, input().split())
l = list(range(1, n+1))

nl = []
idx = 0

while l:
    idx = (idx + k - 1) % len(l)
    nl.append(l.pop(idx))

print("<" + ", ".join(map(str, nl)) + ">")

#from collections import deque

#n, k = map(int, input().split())
#dq = deque(range(1, n+1))
#ans = []

#while dq:
#    dq.rotate(-(k-1))
#    ans.append(dq.popleft())

#print("<" + ", ".join(map(str, ans)) + ">")
