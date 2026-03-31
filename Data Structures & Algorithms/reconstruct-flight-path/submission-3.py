from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        #dfs with edges
        tickets.sort()
        adj = {s:[] for s,d in tickets}
        for s,d in tickets:
            adj[s].append(d)
        res = ["JFK"]
        def dfs(airport):
            if len(res)==len(tickets)+1:
                return True        
            if airport not in adj:
                return
            for i,child in enumerate(adj[airport].copy()):
                res.append(child)
                adj[airport].pop(i)
                if dfs(child):
                    return True
                adj[airport].insert(i,child)
                res.pop()

        
        dfs("JFK")
        return res
