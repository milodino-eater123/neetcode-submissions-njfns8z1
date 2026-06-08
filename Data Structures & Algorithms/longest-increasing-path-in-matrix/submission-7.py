class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n,m=len(matrix),len(matrix[0])
        hmap,visited,res={},set(),0
        def dfs(i,j,prev):
            if i<0 or j<0 or i==n or j==m:
                return 0
            if matrix[i][j]<=prev:
                return 0
            if (i,j) in visited:
                return 0
            if (i,j) in hmap:
                return hmap[(i,j)]
            visited.add((i,j))
            cur=matrix[i][j]
            best = 1 + max(dfs(i+1,j,cur),dfs(i-1,j,cur),dfs(i,j+1,cur),dfs(i,j-1,cur))
            visited.remove((i,j))
            hmap[(i,j)]=best
            return best
        for i in range(n):
            for j in range(m):
                res=max(res,dfs(i,j,float("-inf")))
        return res
