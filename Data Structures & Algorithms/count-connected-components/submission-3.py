from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = 0
        visited = set()
        adj = defaultdict(list)
        for edge in edges:
            one, two = edge
            adj[one].append(two)
            adj[two].append(one)
        
        def dfs(node):
            nonlocal visited
            if node in visited:
                return
            visited.add(node)
            for n in adj[node]:
                dfs(n)
        
        for key in adj.keys():
            if key not in visited:
                res += 1
                dfs(key)
        
        stragglers = n - len(visited)
        return res + stragglers


        