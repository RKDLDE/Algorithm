N = int(input())

def meeting_key(x):
    return (x[1], x[0])

times = sorted([list(map(int, input().split())) for _ in range(N)], key=meeting_key)

cnt = 0
end_time = 0

for start, end in times:
    if start >= end_time:
        cnt += 1
        end_time = end

print(cnt)