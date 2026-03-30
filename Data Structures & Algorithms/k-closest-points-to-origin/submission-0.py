from math import sqrt
from heapq import heapify,heappop,heappush
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def calcDistance(point):
            return sqrt((point[0])**2 + (point[1])**2)
        
        res = []
        for point in points:
            heappush(res,[-calcDistance(point),point])
            if len(res) > k:
                heappop(res)

        return [x[1] for x in res]

        

        