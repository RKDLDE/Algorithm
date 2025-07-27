def solution(arr):
    answer = []
    
    for i in arr:
        if i % 2 == 0 and i >= 50:
            i //= 2
        elif i % 2 != 0 and i < 50:
            i *= 2
        
        answer.append(i)
    return answer