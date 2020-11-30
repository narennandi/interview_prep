def gameOflife(board):

    """
    Do not return anything, modify board in-place instead.
    """
    """
    Encoding Rule
    Dead:         0
    Live:         1
    Live -> Dead: 3
    Dead -> Live: 2
    
    """
    
    def update(x, y):
        live = 0
        for dx in [-1,0,1]:
            for dy in [-1,0,1]:
                if not (dx == 0 and dy==0):
                    # based on the encoding rule, if the current state is live then it will be odd, else it is dead.
                    live += board[x+dx][y+dy]%2 if 0<=x+dx<m and 0<=y+dy<n else 0
        if board[x][y] == 0 and live==3:
            board[x][y] = 2
        elif board[x][y] == 1 and (live<2 or live>3):
            board[x][y] = 3
            
    
    def recover(x, y):
        if board[x][y] == 2:
            board[x][y] = 1
        elif board[x][y] == 3:
            board[x][y] = 0
            
    
    m, n = len(board), len(board[0])
    
    for i in range(m):
        for j in range(n):
            update(i,j)

    for i in range(m):
        for j in range(n):
            recover(i,j)
    return board

if __name__ == '__main__':
    board = [
            [0,1,0],
            [0,0,1],
            [1,1,1],
            [0,0,0]
            ]
    board = gameOflife(board)    
    print(board)