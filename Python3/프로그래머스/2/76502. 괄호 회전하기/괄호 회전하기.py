from collections import deque

def solution(s):
    pairs = {')':'(', ']':'[', '}':'{'}
    deque_s = deque(s)
    cnt = 0
    
    for _ in range(len(s)):
        stack_s = []
        flag = True
        
        for ch in deque_s:
            if ch in pairs.values():
                stack_s.append(ch)
            else:
                if not stack_s or pairs[ch] != stack_s[-1]:
                    flag = False
                    break
                stack_s.pop()
        
        if not stack_s and flag:
            cnt += 1
            
        deque_s.rotate(-1)
        
    return cnt