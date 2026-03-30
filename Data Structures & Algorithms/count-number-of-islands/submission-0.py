class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        n,m = len(grid),len(grid[0])
        visitedIslands = set()
        def dfs(i,j):
            nonlocal visitedIslands
            if i<0 or j<0 or i>=n or j>=m:
                return 
            if (i,j) in visitedIslands:
                return 
            if grid[i][j] == "0":
                return 

            visitedIslands.add((i,j))
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and (i,j) not in visitedIslands:
                    res += 1 
                    dfs(i,j)

        return res


        