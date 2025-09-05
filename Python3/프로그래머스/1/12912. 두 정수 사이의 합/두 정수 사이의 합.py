def solution(a, b):
    s = [x for x in range(min(a, b), max(a, b)+1)]
    return sum(s)