def minSubArrayLen(nums, s):
    left = 0
    right = 0
    res = float('inf')
    summation = 0
    
    while left < len(nums) and right < len(nums):
        # advance right pointer until sum >= s 
        while summation < s and right < len(nums):
            summation += nums[right]
            right += 1
        # advance leftt pointer until sum < s
        while summation >= s:
            res = min(res, right - left)
            summation -= nums[left]
            left += 1
    
    return res if res != float('inf') else 0

nums = [2,3,1,2,4,3]
s= 7
res= minSubArrayLen(nums, s)
print(res)