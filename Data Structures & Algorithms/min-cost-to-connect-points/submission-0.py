from heapq import heappop, heappush
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def calcDistance(p1,p2):
            x1,y1 = p1
            x2,y2 = p2
            return abs(x1-x2)+abs(y1-y2)
        visited = set()
        res = 0
        minHeap = [(0,points[0])]
        while minHeap:
            dist,point = heappop(minHeap)
            if tuple(point) in visited:
                continue
            res += dist
            visited.add(tuple(point))
            for pt in points:
                if tuple(pt) in visited:
                    continue
                dst = calcDistance(pt,point)
                heappush(minHeap,(dst,pt))
        
        return res



        

        