class Solution:
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
    
    