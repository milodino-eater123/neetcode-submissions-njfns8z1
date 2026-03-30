from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #make adj list
        adj = defaultdict(list)
        for u,v,t in times:
            adj[u].append((v,t))
        
        #list of distance from start
        dist = [float('inf')] * (n+1)
        dist[0] = float('-inf')
        #bfs, update
        def dfs(i,time,visited):
            nonlocal dist
            if i in visited and time>visited[i]:
                return
            dist[i] = min(dist[i],time)
            visited[i] = time
            for child in adj[i]:
                j,t = child
                dfs(j,time+t,visited)

        
        dfs(k,0,{})
        res = max(dist) 
        return res if res != float('inf') else -1
    
        