class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prev,dp = 1,[0]*n
        for i in range(m):
            for j in range(n):
                dp[j]+=prev
                prev=dp[j]
            prev=0
        return dp[n-1]

        
        