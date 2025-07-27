def solution(babbling):
    answer = 0
    able_babbling = ["aya", "ye", "woo", "ma"]
    for i in babbling:
        for j in able_babbling:
            i = i.replace(j, ' ')
        if i.strip() == '':
            answer += 1        
    return answer