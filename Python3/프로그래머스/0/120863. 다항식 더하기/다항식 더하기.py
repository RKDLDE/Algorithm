def solution(polynomial):
    xnum = 0
    const = 0
    
    for c in polynomial.split(' + '): # 공백과 +로 항 나누기
        if c.isdigit(): # c가 숫자면
            const+=int(c) # 상수항 합에 합하기
        else:
            if c=='x': # c가 그냥 x면
                xnum = xnum+1 # 1 더하기
            else:
                xnum+=int(c[:-1]) # x 앞에 있는 숫자 더하기
            
    if xnum and const: # 상수항, x 계수 다 있을 때
        return f"{xnum if xnum != 1 else ''}x + {const}"
    elif xnum: # x 계수만 있을 때
        return f"{xnum if xnum != 1 else ''}x"
    else: # 상수항만 이루어져있을 때
        return str(const)