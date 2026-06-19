from heapq import heapify,heappush,heappop
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g,s = [-x for x in g],[-x for x in s]
        heapify(g)
        heapify(s)
        res = 0
        while g and s:
            if -s[0]>=-g[0]:
                res += 1
                heappop(g)
                heappop(s)
            else:
                heappop(g)
        return res

        