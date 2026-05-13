class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def island(i,j):
            if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]):
                return False
            
            if grid[i][j] == "0":
                return False
            
            grid[i][j] = "0"

            island(i+1,j)
            island(i-1,j)
            island(i,j+1)
            island(i,j-1)

            return True
    
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                res += int(island(i,j))
    
        return res
        