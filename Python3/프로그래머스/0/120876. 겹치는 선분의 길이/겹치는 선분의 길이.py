def solution(lines):
    cnt = [0] * 201
    for x1, x2 in lines:
        for i in range(min(x1, x2), max(x1, x2)):
            cnt[i + 100] += 1
    return sum(1 for x in cnt if x >= 2)