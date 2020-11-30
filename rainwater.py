def trap(height):

        l =len(height)
        
        if l == 0:
            return 0
        
        m = 0 
        rain = 0
        temp = 0
        top = max(height)
        
        for i in range(l):
            if height[i] >= m:
                m = height[i]
                rain += temp
                temp = 0
            else:
                temp += m - height[i]
        
        temp = 0
        m = 0
        for i in range(l-1,-1,-1):
            if height[i]==top:
                rain += temp
                break
                
            if height[i] >= m:
                m = height[i]
                rain += temp
                temp = 0
            else:
                temp += m - height[i]

        return rain        

if __name__ == '__main__':
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    res = trap(height)
    print(res)