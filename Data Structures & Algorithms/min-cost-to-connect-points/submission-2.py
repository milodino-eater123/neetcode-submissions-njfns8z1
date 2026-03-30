from heapq import heappop, heappush
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def calcDistance(p1,p2):
            x1,y1 = p1
            x2,y2 = p2
            return abs(x1-x2)+abs(y1-y2)
        visited = set()
        res = 0
        dp = {}
        for point in points:
            dp[tuple(point)] = float('inf')
        dp[tuple(points[0])] = 0
        while dp:
            point = min(dp,key=lambda x:dp[x])
            dist = dp[point]
            res += dist
            del dp[point]
            for pt in points:
                pt = tuple(pt)
                if pt not in dp:
                    continue
                dst = calcDistance(pt,point)
                dp[pt] = min(dst,dp[pt])
        
        return res



        

        

        

        


        

        