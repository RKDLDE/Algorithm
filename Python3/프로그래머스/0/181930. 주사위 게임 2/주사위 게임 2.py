def solution(a, b, c):
    answer = 0
    
    if a == b: answer += 1
    if a == c: answer += 1
    if b == c: answer += 1
    
    if answer == 0: return a + b + c
    elif answer == 1: return (a + b + c) * (a**2 + b**2 + c**2)
    elif answer == 3: return (a + b + c) * (a**2 + b**2 + c**2) * (a**3 + b**3 + c**3)