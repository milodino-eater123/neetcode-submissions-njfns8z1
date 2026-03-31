from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj=defaultdict(list)
        tickets.sort()
        for s,d in tickets[::-1]:
            adj[s].append(d)
        res = []
        def dfs(flight):
            while adj[flight]:
                d = adj[flight].pop()
                dfs(d)
            
            res.append(flight)


        dfs("JFK")
        return res[::-1]
        



        