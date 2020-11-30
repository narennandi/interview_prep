def maxArea(height):
    answer = 0
    left = 0
    right = int(len(height)-1)
    
    while left != right:
        n = height[left]
        m = height[right]
        distance = right-left
        
        if(n < m):
            vertical = (distance) * n 
            left = left+1
        else:
            vertical = (distance) * m
            right = right - 1
        
        answer = answer if answer > vertical else vertical
    
    return answer

height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))