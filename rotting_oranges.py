import collections
def orangesRotting(grid):

    def neighbors(r, c):
        for nr, nc in ((r-1,c),(r,c-1),(r+1,c),(r,c+1)):
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                yield nr, nc

    # queue - all starting cells with rotting oranges
    queue = collections.deque()
    # for r, row in enumerate(grid):
    #     for c, val in enumerate(row):
    #         if val == 2:
    #             queue.append((r, c, 0))        
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 2:
                queue.append((i, j, 0))
    print(queue)

    #DFS solution
    d = 0
    while queue:
        r, c, d = queue.popleft()
        for nr, nc in neighbors(r, c):
            if grid[nr][nc] == 1:
                grid[nr][nc] = 2
                queue.append((nr, nc, d+1))

    if any(1 in row for row in grid):
        return -1
    return d

grid = [[2,1,1],[1,1,0],[0,1,1]]
print(orangesRotting(grid))