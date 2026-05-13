class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n,m = len(grid),len(grid[0])
        def island(i,j):
            nonlocal n,m
            if i<0 or j<0 or i>=n or j>=m or grid[i][j]==0:
                return 0
            
            grid[i][j] = 0
            return 1+island(i+1,j)+island(i-1,j)+island(i,j+1)+island(i,j-1)
        
        res = 0
        for i in range(n):
            for j in range(m):
                res = max(res,island(i,j))
        
        return res
        