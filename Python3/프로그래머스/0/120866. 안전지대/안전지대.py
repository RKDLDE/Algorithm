def solution(board):
    
    # 위, 아래, 좌, 우, 대각선 위치 구하기용
    directions = [(1,0), (0,1), (-1,0), (0,-1), (1,1), (1, -1), (-1,1), (-1,-1)]
    
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                for dx, dy in directions:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < len(board) and 0 <= ny < len(board) and board[nx][ny] == 0:
                        board[nx][ny] = 2
    return sum(row.count(0) for row in board)