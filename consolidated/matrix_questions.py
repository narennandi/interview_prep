def numIslands(grid):
    #Given an m x n 2d grid map of '1's (land) and '0's (water), return the number of islands.
    if grid == None:
        return None
    
    #Helper function to get neighbors
    def neighbors(r,c):
        for nr, nc in ((r, c+1),(r-1,c),(r+1,c),(r,c-1)):
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                yield nr, nc


    #Breath first search
    def doBfs(i, j):
        queue = []
        queue.append((i,j))           
        
        while queue:
            r,c = queue.pop()
            grid[r][c] = 'v'
            
            for nr, nc in neighbors(r, c):
                if grid[nr][nc] == '1':
                    queue.append((nr, nc))
    
    #Depth First search
    def doDfs(r,c):
        if grid[r][c] == 'v':
            return
        else:
            grid[r][c] = 'v'
        
        for nr, nc in neighbors(r,c):
            if grid[nr][nc] == '1':
                doDfs(nr, nc)
    
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                doBfs(i, j)
                count += 1
                
    return count


def orangesRotting(self, grid: List[List[int]]) -> int:
    """
    the value 0 representing an empty cell
    the value 1 representing a fresh orange
    the value 2 representing a rotten orange

    Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.
    Return the minimum number of minutes that must elapse until no cell has a fresh orange.  
    If this is impossible, return -1 instead.
    """
    import collections
    
    def neighbors(r,c):
        for nr, nc in ((r-1,c),(r+1,c),(r, c-1),(r,c+1)):
            if 0<= nr < len(grid) and 0 <= nc < len(grid[0]):
                yield nr, nc
                
    #find all locations where there are rotten cells
    #and add them to queue
    queue= collections.deque()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 2:
                queue.append((i,j,0))
    
    #loop through these cells and check neighbors for 
    #rotten cells
    count = 0
    while queue:
        r,c,count = queue.popleft()
        for nr, nc in neighbors(r,c):
            if grid[nr][nc] == 1:
                grid[nr][nc] = 2   
                queue.append((nr, nc, count+1))
    
    
    if any(1 in row for row in grid):
        return -1        
    return count

def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    """
    Search a 2D Matrix
    Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
    Integers in each row are sorted from left to right.
    The first integer of each row is greater than the last integer of the previous row.
    """
    if not matrix or target is None:
        return False
    
    rows, cols = len(matrix), len(matrix[0])
    left, right = 0, rows * cols - 1
    #Using Binary search
    while left <= right:
        mid = (left + right) // 2
        num = matrix[mid // cols][mid % cols]
        
        if num == target:
            return True
        elif num < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return False

class Solution:
    """
    Search a 2D Matrix II
    Write an efficient algorithm that searches for a target value in an m x n integer matrix. The matrix has the following properties:
    
    Integers in each row are sorted in ascending from left to right.
    Integers in each column are sorted in ascending from top to bottom.
    """
    def binary_search(self, matrix, target, start, vertical):
        lo = start
        hi = len(matrix[0]) - 1 if vertical else len(matrix) - 1
        
        while lo <= hi:
            mid = (lo + hi) // 2
            if vertical: #searching a column
                if matrix[start][mid] < target:
                    lo = mid + 1
                elif matrix[start][mid] > target:
                    hi = mid - 1
                else:
                    return True
                
            else: #searching row
                if matrix[mid][start] < target:
                    lo = mid + 1
                elif matrix[mid][start] > target:
                    hi = mid - 1
                else:
                    return True
        
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
            
        #iterate over diagonals of matrix starting in bottom left.
        for i in range(min(len(matrix), len(matrix[0]))):
            vertical_found = self.binary_search(matrix, target, i, True)
            horizontal_found = self.binary_search(matrix, target, i, False)
            
            if vertical_found or horizontal_found:
                return True
        
        return False

