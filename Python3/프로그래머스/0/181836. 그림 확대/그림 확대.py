def solution(picture, k):
    answer = []
    
    for i in picture:
        c = ''.join(ch * k for ch in i)
        answer.extend([c] * k)
            
    return answer