def solution(numlist, n):
    return sorted(numlist, key=lambda x:(abs(x-n), -x)) # -x: 내림차순