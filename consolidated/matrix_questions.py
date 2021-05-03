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

# 64. Minimum Path Sum
class Solution:
    """
    Approach 1: Brute Force
    The Brute Force approach involves recursion. For each element, we consider two paths, 
    rightwards and downwards and find the minimum sum out of those two. 
    It specifies whether we need to take a right step or downward step to minimize the sum.

    Time complexity : O(2^{m+n})
    For every move, we have atmost 2 options.
    Space complexity : O(m+n). Recursion of depth m+n.
    """
    def minPathSum(self, grid: List[List[int]]) -> int:
        return self.calculate(grid, 0 ,0)
        
    def calculate(self, grid, i, j):
        if i == len(grid) or j == len(grid[0]):
            return float('inf')
        
        if i == len(grid) - 1 and j == len(grid[0]) - 1:
            return grid[i][j]
        
        return grid[i][j] + min(self.calculate(grid, i+1, j), self.calculate(grid, i, j + 1))
    
    """
    Approach 2: Dynamic Programming 2D Algorithm

    We use an extra matrix dpdp of the same size as the original matrix. 
    In this matrix, dp(i, j)dp(i,j) represents the minimum sum of the path from the index (i, j)(i,j) to the bottom rightmost element. 
    We start by initializing the bottom rightmost element of dpdp as the last element of the given matrix. 
    Then for each element starting from the bottom right, we traverse backwards and fill in the matrix with the required minimum sums. 
    Now, we need to note that at every element, we can move either rightwards or downwards. 
    Therefore, for filling in the minimum sum, we use the equation:
    dp(i, j)= grid[i][j] + min(dp(i+1,j),dp(i,j+1))
    
    Time complexity : O(mn) We traverse the entire matrix once.
    Space complexity : O(mn) Another matrix of the same size is used.
    """
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        
        for i in range(len(grid)-1, -1, -1):
            for j in range(len(grid[0])-1, -1, -1):
                
                if i == len(grid) - 1 and j != len(grid[0]) - 1:
                    dp[i][j] = grid[i][j] + dp[i][j+1]
                    
                elif i!= len(grid) - 1 and j == len(grid[0]) - 1:
                    dp[i][j] = grid[i][j] + dp[i+1][j]
                    
                elif i!= len(grid) -1 and j!= len(grid[0]) - 1:
                    dp[i][j] = grid[i][j] + min(dp[i+1][j], dp[i][j+1])
                
                else:
                    dp[i][j] = grid[i][j]
                    
        return dp[0][0]
    
    """
    Approach 3: Dynamic Programming (Without Extra Space)
    This approach is same as Approach 2, with a slight difference. 
    Instead of using another dpdp matrix. We can store the minimum sums in the original matrix itself, 
    since we need not retain the original matrix here. Thus, the governing equation now becomes:
    grid(i, j)= grid[i][j] + min(grid[i+1][j], grid[i][j+1])
    
    Time complexity : O(mn)O(mn). We traverse the entire matrix once.
    Space complexity : O(1)O(1). No extra space is used.
    """
    def minPathSum(self, grid: List[List[int]]) -> int:
        for i in range(len(grid) -1, -1, -1):
            for j in range(len(grid[0])-1,-1,-1):
                
                if i == len(grid) - 1 and j != len(grid[0]) -1:
                    grid[i][j] = grid[i][j] + grid[i][j+1]
                    
                elif i != len(grid) - 1 and j == len(grid[0]) - 1:
                    grid[i][j] = grid[i][j] + grid[i+1][j]
                    
                elif i != len(grid) - 1 and j != len(grid[0]) - 1:
                    grid[i][j] = grid[i][j] + min(grid[i+1][j], grid[i][j+1])
        
        return grid[0][0]

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """
        There are n cities. Some of them are connected, while some are not. 
        If city a is connected directly with city b, 
        and city b is connected directly with city c, 
        then city a is connected indirectly with city c.

        A province is a group of directly or indirectly connected cities and no other cities outside of the group.

        You are given an n x n matrix isConnected where isConnected[i][j] = 1 
        if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

        Return the total number of provinces.
        
        Time complexity : O(n^2) 
        The complete matrix of size n^2n 2 is traversed.

        Space complexity : O(n) visited array of size nn is used.


        """
        rows = len(isConnected)
        seen = set()
        
        def dfs(node):
            for idx, val in enumerate(isConnected[node]):
                if val == 1 and idx not in seen:
                    seen.add(idx)
                    dfs(idx)
            
        count = 0
        for i in range(rows):
            if i not in seen:
                dfs(i)
                count += 1
            
        return count

