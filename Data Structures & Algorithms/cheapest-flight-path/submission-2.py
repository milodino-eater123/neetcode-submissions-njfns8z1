from heapq import heappop,heappush
from collections import defaultdict
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for airport1,airport2,cost in flights:
            adj[airport1].append((cost,airport2))
        
        costs = [float('inf')] * n
        stack = [(0,src)]
        for i in range(k+2):
            newStack = []
            while stack:
                cost,airport = stack.pop()
                if cost >= costs[airport]:
                    continue
                costs[airport] = cost
                for cst,airprt in adj[airport]:
                    newStack.append((cost+cst,airprt))
            stack = newStack
        
        return costs[dst] if costs[dst] != float('inf') else -1
        