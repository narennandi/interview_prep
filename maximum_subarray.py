def maxSubArray(nums):
    #Pick the locally optimal move at each step, 
    # and that will lead to the globally optimal solution.
    max_sum = curr_sum = nums[0]

    for i in range(1, len(nums)):
        curr_sum = max(nums[i], nums[i]+ curr_sum)
        max_sum = max(curr_sum, max_sum)
    
    return max_sum

if __name__ == '__main__':
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(maxSubArray(nums))