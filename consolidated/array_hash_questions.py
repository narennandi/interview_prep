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
                return [memo[num], index]

# 167. Two Sum II - Input array is sorted
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        
        while left < right:
            res = numbers[left] + numbers[right]
            
            if res == target:
                return [left+1, right+1]
            
            elif res < target:
                left += 1
            
            else:
                right -= 1
        
        return []

def isAlienSorted(self, words: List[str], order: str) -> bool:
    """
    In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. 
    The order of the alphabet is some permutation of lowercase letters.
    Given a sequence of words written in the alien language, and the order of the alphabet, 
    return true if and only if the given words are sorted lexicographicaly in this alien language.

    Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
    Output: true
    Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.    

    Complexity Analysis
    Time Complexity: O(C), where C is the total content of words.
    Space Complexity: O(1)
    """
    #create a dict where the key is the letter, value is index of the letter
    order_map = {c:i for i, c in enumerate(order)}
    
    #loop through the words
    for i in range(len(words) - 1):
        word1 = words[i]
        word2 = words[i+1]
        
        #Find the first diff between word1[l] != word2[l]
        for letter in range(min(len(word1), len(word2))):
            if word1[letter] != word2[letter]:
                if order_map[word1[letter]] > order_map[word2[letter]]:
                    return False
                break
            
        else:
            if len(word1) > len(word2):
                return False

    return True

def isHappy(self, n: int) -> bool:
    """
    Write an algorithm to determine if a number n is "happy".
    A happy number is a number defined by the following process: Starting with any positive integer, 
    replace the number by the sum of the 
    squares of its digits, 
    and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. 
    Those numbers for which this process ends in 1 are happy numbers.

    Return True if n is a happy number, and False if not.
    """
    def get_next(n):
        res = 0
        while n > 0:
            n, digits = divmod(n, 10)
            res += digits ** 2
        return res
    
    # Approach 1: Detect Cycles with a HashSet
    # O(logn)
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = get_next(n)
    return n == 1

    # Approach 2: Floyd's Cycle-Finding Algorithm
    # O(logn)
    slow_runner = n
    fast_runner = get_next(n)
    while fast_runner != 1 and slow_runner != fast_runner:
        slow_runner = get_next(slow_runner)
        fast_runner = get_next(get_next(fast_runner))
    return fast_runner == 1


def isValid(self, s: str) -> bool:
    """
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
    An input string is valid if:
        Open brackets must be closed by the same type of brackets.
        Open brackets must be closed in the correct order.
    """
    stack = []
    
    mapping = {
        ")":"(",
        "}":"{",
        "]":"["
    }
    
    for char in s:
        if char not in mapping:
            stack.append(char)
        
        else:
            top_element = stack.pop() if stack else "#"
            
            if mapping[char] != top_element:
                return False
            
    return not stack

def reverse(self, x: int) -> int:
    """
    Given a 32-bit signed integer, reverse digits of an integer.
    """
    res = 0
    remains = abs(x)
    sign = -1 if x < 0 else 1 
    
    while True:
        digit = remains % 10
        res = (res * 10) + digit
        remains = remains // 10
        if remains == 0:
            break
            
    res *= sign
    
    if abs(res) > 0x7FFFFFFF:
        return 0
    else:
        return res

# 811. Subdomain Visit Count
class Solution:
    """
    A website domain like "discuss.leetcode.com" consists of various subdomains. 
    At the top level, we have "com", at the next level, we have "leetcode.com", and at the lowest level, "discuss.leetcode.com". When we visit a domain like "discuss.leetcode.com", 
    we will also visit the parent domains "leetcode.com" and "com" implicitly.
    Example 1:
    Input: 
    ["9001 discuss.leetcode.com"]
    Output: 
    ["9001 discuss.leetcode.com", "9001 leetcode.com", "9001 com"]
    """
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        ans = collections.Counter()
        for domain in cpdomains:
            count, domain = domain.split()
            count = int(count)
            frags = domain.split('.')
            
            for i in range(len(frags)):
                ans[".".join(frags[i:])] += count
        
        return ["{} {}".format(ct, dom) for dom, ct in ans.items()]

# 14. Longest Common Prefix
class Solution:
    """
    Write a function to find the longest common prefix string amongst an 
    array of strings.
    If there is no common prefix, return an empty string ""
    Input: strs = ["flower","flow","flight"]
    Output: "fl"
    """
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if not strs:
            return ""
        
        shortest = min(strs, key = len)
        
        for i, ch in enumerate(shortest):
            for other in strs:
                
                if ch != other[i]:
                    return shortest[:i]
        
        return shortest

class Solution:
    """
    Write a program that outputs the string representation of numbers from 1 to n.
    But for multiples of three it should output “Fizz” instead of the number and 
    for the multiples of five output “Buzz”. For numbers which are multiples of 
    both three and five output “FizzBuzz”.
    n = 15
    ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
    """
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                res.append("FizzBuzz")
            elif i % 3 == 0:
                res.append("Fizz")
            elif i % 5 == 0:
                res.append("Buzz")
            else:
                res.append(str(i))
                
        return res

# 283. Move Zeroes
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Given an array nums, write a function to move all 0's to the end of it 
        while maintaining the relative order of the non-zero elements.

        Example:

        Input: [0,1,0,3,12]
        Output: [1,3,12,0,0]
        Do not return anything, modify nums in-place instead.
        """
        index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[index] = nums[i]
                index += 1
                
        for i in range(index, len(nums)):
            nums[i] = 0


class Solution:
    # 1480. Running Sum of 1d Array
    """
    Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
    Return the running sum of nums.
    """
    def runningSum(self, nums: List[int]) -> List[int]:

        i = 1        
        while i < len(nums):
            nums[i] += nums[i-1]
            i += 1

        return nums