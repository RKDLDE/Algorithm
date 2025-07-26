def solution(keyinput, board):
    answer = [0, 0]
    move = {"up": [0, 1], "down" : [0, -1], "left" : [-1, 0], "right" : [1,0]}
    
    for i in keyinput:
        x, y = move[i]
        
        new_x = answer[0] + x
        new_y = answer[1] + y
        
        if abs(new_x) <= (board[0] // 2) and abs(new_y) <= (board[1] // 2):
            answer = [new_x, new_y]
        
    return answer