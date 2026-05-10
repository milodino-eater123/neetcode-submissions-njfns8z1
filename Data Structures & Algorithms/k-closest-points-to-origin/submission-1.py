import math
from heapq import heappush,heappop
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        for p in points:
            dist = math.sqrt(p[0]**2+p[1]**2)
            heappush(maxHeap,(-dist,p))
            if len(maxHeap) > k:
                heappop(maxHeap)
        
        return [x[1] for x in maxHeap]

