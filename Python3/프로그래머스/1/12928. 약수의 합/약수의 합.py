def solution(n):
    d = [x for x in range(1, n+1) if n % x == 0]
    return sum(d)