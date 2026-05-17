class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def path(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            if i<0 or j<0 or i>=m or j>=n:
                return 0
            
            if i == m-1 and j==n-1:
                return 1
             
            ways = path(i+1,j) + path(i,j+1)
            memo[(i,j)] = ways
            return ways

        
        return path(0,0)

        