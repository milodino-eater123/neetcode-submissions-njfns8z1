from collections import defaultdict
from heapq import heappush,heappop
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #make adj list
        adj = defaultdict(list)
        for u,v,t in times:
            adj[u].append((v,t))
        
        res = 0
        visited = set()
        minHeap = [(0,k)]
        while minHeap:
            cost,node = heappop(minHeap)
            if node in visited:
                continue
            res = cost
            visited.add(node)
            for child,childCost in adj[node]:
                heappush(minHeap,(cost+childCost,child))
        
        return res if len(visited)==n else -1

    
        