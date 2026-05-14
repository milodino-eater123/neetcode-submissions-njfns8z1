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
                return 
            
            hset.add(node)
            for child in al[node]:
                dfs(child)
        
        for i in range(n):
            if i in hset:
                continue
            dfs(i)
            res += 1
        
        return res
        
        
            



        