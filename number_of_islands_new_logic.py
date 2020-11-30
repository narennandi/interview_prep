import collections

def numIslands(grid):
    if grid == None:
        return None

    def doBfs(i, j):
        queue = []
        queue.append((i,j))

        while queue:
            r,c = queue.pop()
            grid[r][c] = "v"

            for nr, nc in neighbors(r,c):
                if grid[nr][nc] == 1:
                    queue.append((nr, nc))

    def neighbors( r,c):
        for nr, nc in ((r-1,c), (r,c-1), (r+1,c), (r,c+1)):
            if 0<= nr < len(grid) and 0 <= nc < len(grid[0]):
                yield nr, nc

    count = 0        
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                doBfs(i, j)
                count += 1
    return count

grid = [[1,0,0],
        [1,0,1]]

print(numIslands(grid))