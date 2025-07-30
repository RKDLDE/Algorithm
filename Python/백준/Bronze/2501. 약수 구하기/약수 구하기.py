N, k = map(int, input().split())
arr = [i for i in range(1, N+1) if N % i == 0]

if len(arr) >= k:
    print(arr[k-1])
else:
    print(0)