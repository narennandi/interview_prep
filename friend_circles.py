def findCircleNum(M):
    seen = set()
    rows = len(M)

    def dfs(node):
        for nei, val in enumerate(M[node]):
            if val == 1 and nei not in seen:
                seen.add(nei)
                # print(seen)
                dfs(nei)
    
    count = 0
    for i in range(rows):
        if i not in seen:
            dfs(i)
            count += 1
            
    return count

M = [[1,1,0],[1,1,0],[0,0,1]]
print(findCircleNum(M))