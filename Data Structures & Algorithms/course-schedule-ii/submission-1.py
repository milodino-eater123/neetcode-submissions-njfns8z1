from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegrees = [0] * numCourses
        adj = defaultdict(set)
        for a,b in prerequisites:
            indegrees[a] += 1
            adj[b].add(a)
        res = []
        stack = [i for i in range(len(indegrees)) if indegrees[i]==0]

        while stack:
                n = stack.pop()
                res.append(n)
                for dependent in adj[n]:
                    indegrees[dependent] -= 1 
                    if indegrees[dependent] == 0:
                        stack.append(dependent)

        
        return res if len(res) == numCourses else []

        