class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        hmap = {}
        n,m = len(matrix),len(matrix[0])
        def dfs(i,j,prev):
            if i<0 or j<0 or i==n or j==m:
                return 0
            if matrix[i][j]<=prev:
                return 0
            if (i,j) in hmap:
                return hmap[(i,j)]
            
            cur = matrix[i][j]
            p1 = dfs(i+1,j,cur)
            p2 = dfs(i-1,j,cur)
            p3 = dfs(i,j+1,cur)
            p4 = dfs(i,j-1,cur)

            res = 1 + max(p1,p2,p3,p4)
            hmap[(i,j)]=res
            return res
        
        res = 0
        for i in range(n):
            for j in range(m):
                res = max(res,dfs(i,j,float("-inf")))
        
        return res
        
