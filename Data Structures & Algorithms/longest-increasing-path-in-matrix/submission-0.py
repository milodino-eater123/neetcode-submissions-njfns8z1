class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        hmap = {}
        res = 0
        n,m = len(matrix),len(matrix[0])
        def dfs(i,j,prev):
            nonlocal hmap
            if i<0 or j<0 or i>=n or j>=m:
                return 0
            if matrix[i][j] <= prev:
                return 0 
            if (i,j) in hmap:
                return hmap[(i,j)]
            
            cur = matrix[i][j]

            up = 1+dfs(i-1,j,cur)
            down = 1+dfs(i+1,j,cur)        
            left = 1+dfs(i,j-1,cur)        
            right = 1+dfs(i,j+1,cur)  

            best = max(up,down,left,right)
            hmap[(i,j)] = best
            return best

        for i in range(n):
            for j in range(m):
                res = max(res,dfs(i,j,-1))

        return res

