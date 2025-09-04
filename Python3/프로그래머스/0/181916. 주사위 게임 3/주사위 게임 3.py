def solution(a, b, c, d):
    dice = [0] * 7
    
    for i in (a, b, c, d):
        dice[i] += 1

    if 4 in dice:
        return 1111 * dice.index(4)
    
    elif 3 in dice:
        return (10 * dice.index(3) + dice.index(1))**2
    
    # 2개 개수
    cnt_2 = [i for i, c in enumerate(dice) if c == 2]
    
    # 두 개씩 같은 값
    if len(cnt_2) == 2:
        p, q = cnt_2
        return (p + q) * abs(p - q)

    # 한 쌍만 같은 값
    if len(cnt_2) == 1:
        single = [i for i, c in enumerate(dice) if c == 1]
        q, r = single
        return q * r
    
    # 다 다른 값
    single = [i for i, c in enumerate(dice) if c == 1]
    return min(single)