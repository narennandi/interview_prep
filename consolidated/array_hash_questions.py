def maxSubArray(nums):
    """Given an integer array nums, 
    find the contiguous subarray (containing at least one number) 
    which has the largest sum and return its sum.
    """
    #dynamic programming

    n = len(nums)
    curr_sum = max_sum = nums[0]
    
    for i in range(1,n):
        curr_sum = max(nums[i], curr_sum + nums[i])
        max_sum = max(max_sum, curr_sum)
        
    return max_sum

def plusOne(self, digits: List[int]) -> List[int]:
    """Given an array representing an integer, add one and return
    the new number represented as an array.
    e.g. -> [1, 2, 3, 4] -> [1, 2, 3, 5]
         -> [1, 9, 9] -> [2, 0, 0]
         -> [9, 9, 9] -> [1, 0, 0, 0]
    """
    n = len(digits)
    for i in reversed(range(n)):
        # set all the nines at the end of array to zeros
        if digits[i] == 9:
            digits[i] = 0

        # here we have the rightmost not-nine    
        else:
            # increase this rightmost not-nine by 1
            digits[i] += 1
            #done
            return digits

    # we're here because all the digits are nines
    return [1] + digits

# O(nlgn) time
def firstMissingPositive(self, nums):
    """
    Given an unsorted integer array nums, 
    find the smallest missing positive integer.
    Input: nums = [1,2,0]
    Output: 3
    """
    nums.sort()
    res = 1
    for num in nums:
        if num == res:
            res += 1
    return res

# O(n) time
def firstMissingPositive(nums):
    """
    Given an unsorted integer array nums, 
    find the smallest missing positive integer.
    Input: nums = [1,2,0]
    Output: 3
    """

    n = len(nums)

    # Base case.
    if 1 not in nums:
        return 1

    # nums = [1]
    if n == 1:
        return 2

    # Replace negative numbers, zeros,
    # and numbers larger than n by 1s.
    # After this conversion nums will contain 
    # only positive numbers.
    for i in range(n):
        if nums[i] <= 0 or nums[i] > n:
            nums[i] = 1

    # Use index as a hash key and number sign as a presence detector.
    # For example, if nums[1] is negative that means that number `1`
    # is present in the array. 
    # If nums[2] is positive - number 2 is missing.
    for i in range(n): 
        a = abs(nums[i])
        # If you meet number a in the array - change the sign of a-th element.
        # Be careful with duplicates : do it only once.
        # [3,4,-1,1]
        if a == n:
            nums[0] = - abs(nums[0])
        else:
            nums[a] = - abs(nums[a])
        
    # Now the index of the first positive number 
    # is equal to first missing positive.
    for i in range(1, n):
        if nums[i] > 0:
            return i

    if nums[0] > 0:
        return n

    return n + 1

# O(n)
def majorityElement(self, nums: List[int]) -> int:
    """
    Given an array of size n, find the majority element. 
    The majority element is the element that appears more than ⌊ n/2 ⌋ times.
    """
    import collections
    counts = collections.Counter(nums)
    return max(counts.keys(), key = counts.get)

def isHappy(n):
    """
     Replace the number by the sum of the squares of its digits, 
     and repeat the process until the number equals 1 (where it will stay), 
     or it loops endlessly in a cycle which does not include 1. 
     Those numbers for which this process ends in 1 are happy numbers.
    """
    def check_num(n):
        res = 0
        while n > 0:
            n, digits = divmod(n, 10)
            res += digits ** 2
        return res
    
    
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = check_num(n)
        
    return n == 1

def reverseInteger(x):
    """
    Store the sign separately and reverse the integer by 
    converting it into a string
    """
    sign = [1,-1][x < 0]
    res = sign * int(str(abs(x))[::-1])
    return res if -(2**31) < res < 2**31 else 0


class MinStack:
    """
    Implement a Minstack
    """
    def __init__(self):
        self.stack = []
        

    def push(self, x: int) -> None:
        
        # If the stack is empty, then the min value
        # must just be the first value we add
        if not self.stack:
            self.stack.append((x, x))
            return

        current_min = self.stack[-1][1]
        self.stack.append((x, min(x, current_min)))
        
        print(self.stack)
        
        
    def pop(self) -> None:
        print("Popping")
        self.stack.pop()
        print(self.stack)
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]


class MyQueue:
    """
    Implement Queue using Stacks
    Implement a first in first out (FIFO) queue using only two stacks. 
    The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).
    """
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.inStack = []
        self.outStack = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.inStack.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        self.move()
        return self.outStack.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        self.move()
        return self.outStack[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return (not self.inStack) and (not self.outStack)
        
    def move(self):
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())
  

def connectSticks(A):
    """
    You can connect any two sticks of lengths x and y into one stick by paying a cost of x + y. 
    You must connect all the sticks until there is only one stick remaining.
    Return the minimum cost of connecting all the given sticks into one stick in this way.
    """
    if len(sticks) == 1:
        return 0

    import heapq
    heapq.heapify(sticks)

    cost = 0
    while len(sticks) > 1:
        x, y =  heapq.heappop(sticks), heapq.heappop(sticks)
        cost += x + y
        heapq.heappush(sticks, x+y)

    return cost


def numIdenticalPairs(self, nums: List[int]) -> int:
    """
    Given an array of integers nums.
    A pair (i,j) is called good if nums[i] == nums[j] and i < j.
    Return the number of good pairs.
    """
    #brute force
    # res = 0
    # for i in range(len(nums)):
    #     for j in range(len(nums)):
    #         if i >= j:
    #             continue

    #         if nums[i] == nums[j]:
    #             res += 1
    # return res
    #with memoization
    res = 0
    memo = {}
    
    for n in nums:
        
        if n not in memo:
            memo[n] = 1
        
        else:
            # count number of pairs based on duplicate values
            if memo[n] == 1:
                res += 1
            else:
                res += memo[n]
                
            memo[n] += 1
            
    return res


def numJewelsInStones(self, J: str, S: str) -> int:
    #brute force
    """
    You're given strings J representing the types of stones that are jewels, and S representing the stones you have. 
    Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.
    The letters in J are guaranteed distinct, and all characters in J and S are letters. 
    Letters are case sensitive, so "a" is considered a different type of stone from "A".

    Input: J = "aA", S = "aAAbbbb"
    Output: 3
    """
    res = 0
    for stone in S:
        if stone in J:
            res += 1
    return res
    
    #Optimized by using a Hash set
    res = 0
    jewel_set = set(J)
    for stone in S:
        if stone in jewel_set:
            res += 1 
    return res


def twoSum(self, nums: List[int], target: int) -> List[int]:
    """
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    You can return the answer in any order.
    """
    # res = []
    # for i in range(len(nums)):
    #     for j in range(len(nums)):
    #         if i == j:
    #             continue

    #         if nums[i] + nums[j] == target:
    #             res.append(i)
    #             res.append(j)
    #             return res
        
        memo = {}
        for index, num in enumerate(nums):
            #if target - num is already in memo, then return current index and the num's index
            n = target - num

            if num not in memo:
                memo[n] = index
                
            else:
                return [index, memo[num]]
