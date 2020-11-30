def findJudge(N, trust):
    if len(trust) < N- 1:
        return -1
    
    indegree  = [0] * (N+1)
    outdegree = [0] * (N+1)
    
    for a, b in trust:
        outdegree[a] += 1
        indegree[b] += 1
    
    print(indegree)
    print(outdegree)

trust = [[1,3], [2,3], [4,3], [4,1], [5,3], [5,1], [5,4]]
N =  5
findJudge(N, trust)