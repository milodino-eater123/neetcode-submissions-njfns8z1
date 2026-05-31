from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        al = defaultdict(list)
        for n1,n2 in edges:
            al[n1].append(n2)
            al[n2].append(n1)

        cycle,visited = False,set()
        def dfs(node,prev=None):
            nonlocal cycle
            if node in visited:
                cycle = True
                return
            visited.add(node)
            for child in al[node]:
                if child==prev:
                    continue
                dfs(child,node)   
        dfs(0) 
        if cycle:
            return False
        
        return len(visited) == n
        



