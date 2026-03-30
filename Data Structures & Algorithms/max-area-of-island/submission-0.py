class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        n,m = len(grid),len(grid[0])
        visitedIslands = set()
        def dfs(i,j):
            nonlocal visitedIslands
            if i<0 or j<0 or i>=n or j>=m:
                return 0
            if (i,j) in visitedIslands:
                return 0
            if grid[i][j] == 0:
                return 0

            visitedIslands.add((i,j))
            return 1+dfs(i+1,j)+dfs(i-1,j)+dfs(i,j+1)+dfs(i,j-1)

        for i in range(n):
            for j in range(m):
                res = max(res,dfs(i,j))

        return res
        