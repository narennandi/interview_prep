def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    L = len(nums)
    
    before  = L*[1]
    for i in range(1,L):
        before[i] = nums[i-1] * before[i-1]
    
    after = L*[1]
    for i in reversed(range(0,L-1)):
        after[i] = nums[i+1] * after[i+1]
        
    for i in range(L):
        before[i] = before[i]*after[i]
        
    return before

nums = [1,2,3,4]
print(productExceptSelf(nums))