class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m<n:
            n,m=m,n
        dp=[0]*n
        dp[0]=1
        for i in range(m):
            prev=0
            for j in range(n):
                dp[j]+=prev
                prev=dp[j]
        return dp[n-1]

        
        