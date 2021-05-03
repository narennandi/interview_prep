# 746. Min Cost Climbing Stairs
class Solution:
    """
    On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).
    Once you pay the cost, you can either climb one or two steps. 
    You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.

    Step 1 - Identify a recurrence relation between subproblems. In this problem,
    Recurrence Relation:
    mincost(i) = cost[i]+min(mincost(i-1), mincost(i-2))
    Base cases:
    mincost(0) = cost[0]
    mincost(1) = cost[1]
    """
    
    """
    Step 2 - Covert the recurrence relation to recursion
    Recursive Top Down - O(2^n) Time Limit Exceeded
    """
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        return min(self.minCost(cost, n-1), self.minCost(cost, n-2))
    
    def minCost(self, cost, n):
        if n < 0:
            return 0

        if n == 0 or n == 1:
            return cost[n]

        return cost[n] + min(self.minCost(cost, n-1), self.minCost(cost, n-2))
    
    """
    Step 3 - Optimization - Top Down DP - Add memoization to recursion
    Top Down Memoization - O(n) 1ms
    """
    
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = {}
        return min(self.minCost(cost, n-1, dp), self.minCost(cost, n-2, dp))
    
    def minCost(self, cost, n, dp):
        
        if n < 0:
            return 0
        if n == 0 or n == 1:
            return cost[n]
        
        if n in dp:
            return dp[n]
        
        dp[n] = cost[n] + min(self.minCost(cost, n-1, dp), self.minCost(cost, n-2, dp))
        return dp[n]
    
    """
    Step 4 - Optimization 2 -Bottom Up DP - Convert recursion to iteration - Getting rid of recursive stack
    Bottom up tabulation - O(n) 1ms
    """
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = {}
        
        for i in range(n):
            if i < 2:
                dp[i] = cost[i]
            else:
                dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        
        return min(dp[n-1], dp[n-2])
    
    """
    Step 5 - Optimization 3 - Fine Tuning - Reduce O(n) space to O(1).
    """
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        first = cost[0]
        second = cost[1]
        if (n <= 2):
            return min(first, second)
        
        for i in range(2, n):
            curr = cost[i] + min(first, second)
            first = second
            second = curr
        
        return min(first, second)

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

# 509. Fibonacci Number
class Solution:
    """
    The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, 
    such that each number is the sum of the two preceding ones, starting from 0 and 1. 
    That is,
    F(0) = 0, F(1) = 1
    F(n) = F(n - 1) + F(n - 2), for n > 1.
    Given n, calculate F(n).
    """
    #Approach : recursion
    """
    Time complexity : O(2^N)
    This is the slowest way to solve the Fibonacci Sequence because it takes exponential time. 
    The amount of operations needed, for each level
    of recursion, grows exponentially as the depth approaches N.
    """
    def fib(self, N: int) -> int:
        if N <= 1:
            return N 
        return self.fib(N-1) + self.fib(N-2)
    
    #Approach : Recusrion Approach using Memoization
    """
    Time complexity : O(N) Each number, starting at 2 up to and including N, is visited, computed and then stored for O(1)O(1) access
    later on.
    Solve for all of the sub-problems, use memoization to store the pre-computed answers, then return the answer for N. We will leverage           recursion, but in a smarter way by not repeating the work to calculate existing values.
    """
    def fib(self, N: int) -> int:
        if N <= 1:
            return N
        return self.memoize(N)
    
    def memoize(self, N):
        cache = {
            0:0,
            1:1
        }
        if N in cache:
            return cache[N]
        
        cache[N] = self.memoize(N - 1) + self.memoize(N - 2)
        return cache[N]
     
    #Approach : Bottom-Up Approach Dynamic programming using Memoization
    """
    Complexity Analysis
    Time complexity : O(N) 
    Each number, starting at 2 up to and including N, is visited, computed and then stored for O(1)O(1) access later on.
    """
    def fib(self, N: int) -> int:
        if N <= 1:
            return N
        return self.memoize(N)
    
    def memoize(self, N):
        cache = {
            0:0,
            1:1
        }
        # Since range is exclusive and we want to include N, we need to put N+1.
        for i in range(2, N+1):
            cache[i] = cache[i-1] + cache[i-2]
            
        return cache[N]

#322. Coin Change
class Solution:
    """
    You are given coins of different denominations and a total amount of money amount. 
    Write a function to compute the fewest number of coins that you need to make up that amount. 
    If that amount of money cannot be made up by any combination of the coins, return -1.
    You may assume that you have an infinite number of each kind of coin.
    """

    """
    Brute Force
    Time limit exceeded
    Time complexity : O(S^n) 
    In the worst case, complexity is exponential in the number of the coins nn.
    """
    def coinChange(self, coins: List[int], amount: int) -> int:
        return self.find_num_coins(0, coins, amount)
    
    def find_num_coins(self, idxCoin, coins, amount):
        if amount == 0:
            return 0
        
        if idxCoin < len(coins) and amount > 0:            
            maxValue = amount // coins[idxCoin]
            minCost = float('inf')
            
            for x in range(maxValue + 1):
                res = self.find_num_coins(idxCoin + 1, coins, amount - x * coins[idxCoin])
                
                if res != -1:
                    minCost = min(minCost, res + x)
            
            if minCost == float('inf'):
                return -1
            else:
                return minCost
        
        return -1
    
    """
    Dynamic Programming
    Top-Down approach
    Could we improve the exponential solution above? Definitely! The problem could be solved with polynomial time using Dynamic programming
    technique. First, let's define:
    
    F(S) - minimum number of coins needed to make change for amount SS using coin denominations [c(0)....c(n-1)]
    
    Time complexity : O(S*n)
    Space complexity : O(S)
    """
    def coinChange(self, coins: List[int], amount: int) -> int:
        return self.find_num_coins(coins, amount, {})
    
    def find_num_coins(self, coins, rem_amount, cache):
        if rem_amount < 0:
            return -1
        if rem_amount == 0:
            return 0
        
        if rem_amount - 1 in cache:
            if cache[rem_amount - 1] != 0:
                return cache[rem_amount-1]
        
        minCost = float('inf')
        
        for coin in coins:
            res = self.find_num_coins(coins, rem_amount - coin, cache)
            if res >= 0 and res < minCost:
                minCost = 1 + res
        
        if minCost == float('inf'):
            cache[rem_amount - 1] = -1
        else:
            cache[rem_amount - 1] = minCost
        
        return cache[rem_amount - 1]    
    """
    Approach #3 (Dynamic programming - Bottom up)
    Time complexity : O(S*n)
    Space complexity : O(S)
    """
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for coin in coins:
            for x in range(coin, amount+1):
                dp[x] = min(dp[x], dp[x-coin] + 1)
        
        if dp[amount] != float('inf'):
            return dp[amount]
        else:
            return -1

class NumArray:
    #303. Range Sum Query - Immutable
    """
    Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.
    Implement the NumArray class:
    NumArray(int[] nums) Initializes the object with the integer array nums.
    int sumRange(int i, int j) Return the sum of the elements of the nums array in the range [i, j] inclusive (i.e., sum(nums[i], nums[i + 1], ... , nums[j]))
    """

    """
    Approach #1 (Brute Force) [Time Limit Exceeded]
    Each time sumRange is called, we use a for loop to sum each individual element from index i to j.
    """
    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, i: int, j: int) -> int:
        res = 0
        for x in range(i, j+1):
            res += self.nums[x]
        
        return res
    
    """
    Approach #2 (Caching) [Accepted]
    The above approach takes a lot of space, could we optimize it?

    https://www.youtube.com/watch?v=CjPMfq3ULZg&feature=emb_title
    
    Imagine that we pre-compute the cummulative sum from index 0 to k. 
    Could we use this information to derive Sum(i,j)?
    """
    def __init__(self, nums: List[int]):
        self.res = [0]
        for i in range(len(nums)):
            self.res.append(self.res[i] + nums[i])
    
    def sumRange(self, i: int, j: int) -> int:
        return self.res[j+1] - self.res[i]
    

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

# The goal is to implement `get_numbers` so that it returns all numbers
# of length N that can be created from the path a knight in chess would make in
# N moves on a phone dial pad, starting at position 0.

#recursion + memoization
def get_sequence(number_of_hops, start_position, cache, sequence=None):
    if sequence is None:
        sequence = [start_position]

    if number_of_hops == 0:
        yield sequence
        return

    if ((start_position, number_of_hops)) in cache:
        yield cache[(start_position, number_of_hops)]
        return

    for neighbor in neighbors(start_position):
        yield from get_sequence(number_of_hops - 1, neighbor, cache, sequence + [neighbor])
    cache[(start_position, number_of_hops)] = sequence + [neighbor]

def get_nums(n):
    if n <= 0:
        return []

    start_position = 0
    results = []
    cache = {}
    for sequence in get_sequence(n, start_position, cache):
        results.append(sequence)
    return results

# The goal is to implement `get_sequence_count` so that it returns count of 
# distinct sequeunces that can be created from the path a knight in chess would make in
# N moves on a phone dial pad, starting at position 0.

def neighbors(k):
    d = {
        0: [4, 6],
        1: [8, 6],
        2: [7, 9],
        3: [4, 8],
        4: [0, 3, 9],
        5: [],
        6: [7, 0, 1],
        7: [2 ,6],
        8: [1, 3],
        9: [2 ,4],
    }
    return d[k]

def get_sequence_count(start_position, number_of_hops, cache, sequence = None):
    if sequence is None:
        sequence = [start_position]
    
    if number_of_hops == 0:
        yield sequence
        return

    if ((start_position, number_of_hops)) in cache:
        return cache[(start_position, number_of_hops)]
    
    for neighbor in neighbors(start_position):
        yield from get_sequence_count(neighbor, number_of_hops - 1, cache, sequence + [neighbor])
    cache[(start_position, number_of_hops)] = sequence + [neighbor]

def get_nums_memo(n):
    if n <= 0:
        return []
    
    cache = {}
    start_position = 0
    count = 0
    for sequence in get_sequence_count(start_position, n, cache):
        count += 1
    return count