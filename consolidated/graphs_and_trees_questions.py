# 797. All Paths From Source to Target
# 4.1 Route Between Nodes: Given a directed graph, design an algorithm to find out 
# whether there is a route between two nodes.
class Solution:
    """
    Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, 
    find all possible paths from node 0 to node n - 1, and return them in any order.
    The graph is given as follows: graph[i] is a list of all nodes 
    you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).
    """
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        target = len(graph) - 1
        results = []

        def backtrack(currNode, path):
            # if we reach the target, no need to explore further.
            if currNode == target:
                results.append(list(path))
                return
            # explore the neighbor nodes one after another.
            for nextNode in graph[currNode]:
                path.append(nextNode)
                backtrack(nextNode, path)
                path.pop()
        # kick of the backtracking, starting from the source node (0).
        path = deque([0])
        backtrack(0, path)

        return results


# Minimal Tree: Given a sorted (increasing order) array with unique integer elements, write an algorithm
# to create a binary search tree with minimal height.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    108. Convert Sorted Array to Binary Search Tree
    Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
    For this problem, a height-balanced binary tree is defined as a binary tree 
    in which the depth of the two subtrees of every node never differ by more than 1.

    Time complexity: O(N) since we visit each node exactly once.
    """
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        
        def helper(left, right):
            if left > right:
                return None
            
            # always choose left middle node as a root
            midElem = (left + right) // 2
            
            # preorder traversal: node -> left -> right
            root = TreeNode(nums[midElem])
            root.left = helper(left, midElem - 1)
            root.right = helper(midElem + 1, right)
            
            return root
            
            
        return helper(0, len(nums) - 1)

# 997. Find the Town Judge
class Solution:
    """
    In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the town judge.

    If the town judge exists, then:

    The town judge trusts nobody.
    Everybody (except for the town judge) trusts the town judge.
    There is exactly one person that satisfies properties 1 and 2.
    You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.

    If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.

    Input: N = 2, trust = [[1,2]]
    Output: 2
    """
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        
        if len(trust) < N - 1:
            return -1

        indegree = [0] * (N+1)
        outdegree = [0] * (N+1)
        
        for a, b in trust:
            outdegree[a] += 1
            indegree[b] += 1
            
        for i in range(1, N+1):
            if indegree[i] == N-1 and outdegree[i] == 0:
                return i
            
        return -1