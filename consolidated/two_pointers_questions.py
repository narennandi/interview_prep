def reverseString(self, s: List[str]) -> None:
    """
    Write a function that reverses a string. The input string is given as an array of characters char[].

    Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
    You may assume all the characters consist of printable ascii characters.
    Do not return anything, modify s in-place instead.
    """
    #Iterative approach
    left, right = 0, len(s) - 1
    
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right-= 1
    
    return s

class Solution:
    """
    Time:  O(n)
    Space: O(k)
    [k = length of the longest substring w/o repeating characters]
    Longest Substring Without Repeating Characters
    Given a string s, find the length of the longest substring without repeating characters.
    """
    def lengthOfLongestSubstring(self, string: str) -> int:
        max_length = 0
        left, right = 0, 0
        chars = set()
        
        while left < len(string) and right < len(string):
            
            if string[right] not in chars:
                chars.add(string[right])
                right += 1
                max_length = max(max_length, right - left)
            
            else:
                chars.remove(string[left])
                left += 1
                
        return max_length

def twoSumII(self, numbers: List[int], target: int) -> List[int]:
    """
    Given an array of integers that is already sorted in ascending order, 
    find two numbers such that they add up to a specific target number.
    The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.
    """

    l = 0
    r = len(numbers) - 1
    
    while l < r:
        
        s = numbers[l] + numbers[r]
        
        if s == target:
            return [l + 1, r + 1]
        
        elif s > target:
            r -= 1
            
        else:
            l += 1

class Solution:
    """
    Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
    Notice that the solution set must not contain duplicate triplets. 

    Example 1:
    Input: nums = [-1,0,1,2,-1,-4]
    Output: [[-1,-1,2],[-1,0,1]]
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #sort the array
        nums.sort()
        
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i] != nums[i-1]:
                self.twoSum(nums, i, res)
        
        return res
        
    def twoSum(self, nums, i, res):
        
        l = i + 1
        r = len(nums) - 1
        
        while l < r:
            sum = nums[l] + nums[r] + nums[i]
              
            if sum < 0:
                l += 1
            
            elif sum > 0:
                r -= 1
            
            else:
                res.append([nums[l], nums[r], nums[i]])
                l += 1
                r -= 1
                
                while l < r and nums[l] == nums[l -1]:
                    print(nums[l], nums[l-1])
                    l += 1


class Solution:
    """
    42. Trapping Rain Water (Hard)
    Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining
    """
    def trap(self, height: List[int]) -> int:
        
        waterlevel = []
        
        left = 0
        for h in height:
            left = max(left, h)
            waterlevel.append(left) # filling up water till the end of the building
            
        right = 0
        for i, h in reversed(list(enumerate(height))):
            right = max(right, h)
            waterlevel[i] = min(waterlevel[i], right) - h # draining ou the water 
            
        return(sum(waterlevel))

class Solution:
    def maxArea(self, height: List[int]) -> int:
#         """
#         brute force
#         """
#         res = 0
#         for i in range(len(height)):
#             for j in range(len(height)):
#                 if i >= j:
#                     continue
#                 temp = min(height[i], height[j]) * (j-i)
#                 if temp > res:
#                     res = temp                
#         return res
        """
        Two pointers
        
        11. Container With Most Water
        Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). 
        n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). 
        Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.
        """
        l = 0
        r = len(height) - 1
        res = 0

        while l < r:
            temp = min(height[l], height[r]) * (r - l)
            if temp > res :
                res = temp
                
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
                
        return res

class Solution:
    """
    Given a string S that only contains "I" (increase) or "D" (decrease), let N = S.length.
    Return any permutation A of [0, 1, ..., N] such that for all i = 0, ..., N-1:

    If S[i] == "I", then A[i] < A[i+1]
    If S[i] == "D", then A[i] > A[i+1]
    

    Example 1:

    Input: "IDID"
    Output: [0,4,1,3,2]
    """
    def diStringMatch(self, S: str) -> List[int]:
        lo, hi = 0, len(S)
        
        ans = []
        for x in S:
            if x == 'I':
                ans.append(lo)
                lo += 1
                
            else:
                ans.append(hi)
                hi -= 1
                
        return ans + [lo]