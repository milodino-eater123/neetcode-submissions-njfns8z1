from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegrees = [0] * numCourses
        al = defaultdict(list)
        for a,b in prerequisites:
            al[b].append(a)
            indegrees[a]+=1
        
        res = []
        stack = [i for i in range(numCourses) if indegrees[i]==0]
        while stack:
            course = stack.pop()
            res.append(course)
            for child in al[course]:
                indegrees[child]-=1
                if indegrees[child]==0:
                    stack.append(child)
        
        return res if len(res)==numCourses else []

        
        