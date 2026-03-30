from collections import defaultdict
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        #adj list
        adj = defaultdict(list)
        for edge in edges:
            one,two = edge
            adj[one].append(two)
            adj[two].append(one)

        visited = set()
        cycle = set()
        connector = None
        inCycle = False
        def dfs(node,prev=None):
            nonlocal visited,connector,cycle,inCycle
            if node in visited:
                inCycle = True
                connector = node
                return True
            
            visited.add(node)
            for child in adj[node]:
                if child == prev:
                    continue
                if dfs(child,node):
                    if inCycle:
                        cycle.add(child)
                    if node == connector:
                        inCycle = False
                    return True
            visited.remove(node)
        dfs(1)    
        for one,two in reversed(edges):
            if one in cycle and two in cycle:
                return [one,two]



