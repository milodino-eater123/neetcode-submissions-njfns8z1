class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n,m = len(matrix), len(matrix[0])
        hmap = {}
        def dfs(i,j,prev):
            if i<0 or j<0 or i==n or j==m:
                return 0
            if matrix[i][j]<=prev:
                return 0
            if (i,j) in hmap:
                return hmap[(i,j)]
            val = matrix[i][j]
            ans = 1 + max(dfs(i+1,j,val),dfs(i-1,j,val),dfs(i,j+1,val),dfs(i,j-1,val))
            hmap[(i,j)]=ans
            return ans
        res = 0
        for i in range(n):
            for j in range(m):
                res = max(res,dfs(i,j,float("-inf")))
        return res





        