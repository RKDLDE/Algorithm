def solution(a, b):
    sum = 0
    for aa, bb in zip(a, b):
        sum += aa * bb
    return sum