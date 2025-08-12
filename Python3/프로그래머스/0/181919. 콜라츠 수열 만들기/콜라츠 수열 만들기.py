def solution(n):
    answer = [n]
    while n != 1:
        c = n/2 if n % 2 == 0 else 3 * n + 1
        answer.append(c)
        n = c
    return answer