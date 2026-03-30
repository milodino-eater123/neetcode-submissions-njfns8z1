from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        def findRoot(node):
            while parent[node] != node:
                node = parent[node]
            return node
        def union(a,b):
            rootA = findRoot(a)
            rootB = findRoot(b)
            if rootA != rootB:
                parent[rootA] = rootB
        
        for edge in edges:
            a,b = edge
            union(a,b)

        res = 0
        for node in range(n):
            if parent[node] == node:
                res += 1 
        
        return res

        


        