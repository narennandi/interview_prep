class Solution:
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
    