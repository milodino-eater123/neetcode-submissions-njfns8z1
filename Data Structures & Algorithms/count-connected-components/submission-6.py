class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        al = {i:[] for i in range(n)}
        for n1,n2 in edges:
            al[n1].append(n2)
            al[n2].append(n1)
        
        hset=set()
        res = 0
        def dfs(node):
            if node in hset:
                return False
            
            hset.add(node)
            for child in al[node]:
                dfs(child)
            return True
        
        for i in range(n):
            if dfs(i):
                res += 1
        
        return res
        
        
            



        