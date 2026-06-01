from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = [0] * numCourses
        al = defaultdict(list)
        for a,b in prerequisites:
            al[b].append(a)
            indegrees[a]+=1
        stack = [i for i in range(numCourses) if indegrees[i]==0]
        while stack:
            course = stack.pop()
            for child in al[course]:
                indegrees[child]-=1
                if indegrees[child]==0:
                    stack.append(child)
        
        return not any(indegrees)

