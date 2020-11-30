def rotate(nums, k):
    """
    Do not return anything, modify nums in-place instead.
    """
    for i in range(k):
        nums.insert(0, nums.pop())
    return nums

nums = [1,2,3,4,5,6,7] 
k = 3
print(rotate(nums,k))