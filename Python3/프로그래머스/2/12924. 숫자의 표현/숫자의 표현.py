def solution(n):
    cnt = 0
    
    for i in range(1, n+1):
        sum_val = 0
        for j in range(i, n+1):
            sum_val += j
            if sum_val == n:
                cnt += 1
            elif sum_val > n:
                break
                
    return cnt