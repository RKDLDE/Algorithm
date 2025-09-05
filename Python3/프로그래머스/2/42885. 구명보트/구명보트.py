def solution(people, limit):
    sp = sorted(people)
    
    left = 0
    right = len(sp) - 1
    boat = 0
    
    while left <= right:
        if sp[left] + sp[right] <= limit:
            boat += 1
            left += 1
            right -= 1
        else:
            boat += 1
            right -= 1
            
    return boat