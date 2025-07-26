def solution(n):
    cnt = 0
    num = 0
    while cnt < n:
        num += 1
        
        if num % 3 == 0 or '3' in str(num):
            continue
            
        cnt += 1
    return num