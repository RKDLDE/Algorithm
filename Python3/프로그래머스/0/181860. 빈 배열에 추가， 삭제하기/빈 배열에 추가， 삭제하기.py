def solution(arr, flag):
    answer = []
    
    for a, f in zip(arr, flag):
        if f:
            answer += [a for _ in range(a * 2)]
        else:
            answer = answer[:-a]
                
    return answer