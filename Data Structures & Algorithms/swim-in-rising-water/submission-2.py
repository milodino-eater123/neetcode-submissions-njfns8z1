from heapq import heappush,heappop
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n,m = len(grid),len(grid[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        minHeap = [(grid[0][0],(0,0))]
        res = 0
        visited = set()
        while minHeap:
            cost,cords = heappop(minHeap)
            i,j = cords
            res = max(res,cost)
            visited.add((i,j))
            if cords == (n-1,m-1):
                return res
            for x,y in directions:
                x += i
                y += j
                if x>=0 and y>=0 and x<n and y<m and (x,y) not in visited:
                    heappush(minHeap,(grid[x][y],(x,y)))
  

        