def solution(arr):
    answer = [arr[0]]
    x = arr[0]
    i = 1
    
    while i < len(arr):
        if x != arr[i]:
            x = arr[i]
            answer.append(x)
        i += 1   # 무조건 증가
    return answer