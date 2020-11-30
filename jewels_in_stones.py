def numJewelsInStones(J,S):
    count = {}
    for k in J:
        for v in S:
            if k in count and k == v:
                count[k] += 1
            elif k == v:
                count[k] = 1
            
    res = 0
    for nums in count.values():
        res += nums
            
    return res

J = "aA" 
S = "aAAbbbb"

print(numJewelsInStones(J, S))