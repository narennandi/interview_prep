def minPathSum(grid):
    rows = len(grid)
    cols = len(grid[0])
    for i in reversed(range(rows)):
        for j in reversed(range(cols)):
            if i ==rows - 1 and j ==cols -1:
                continue
            elif i == rows - 1:
                grid[i][j] += grid[i][j+1]
            elif j == cols -1:
                grid[i][j] += grid[i+1][j]
            else:
                grid[i][j] += max(grid[i][j+1], grid[i+1][j])              
    return grid[0][0]

grid =  [
        [1,3,1],
        [1,5,1],
        [4,2,1]
        ]
print(minPathSum(grid))