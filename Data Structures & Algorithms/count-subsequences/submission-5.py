class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        l1,l2 = len(s),len(t)
        dp = [1]*(l1+1)
        dp[-1]=0
        for j in range(l2-1,-1,-1):
            diag=1 if j==l2-1 else 0
            for i in range(l1-1,-1,-1):
                temp=dp[i]
                dp[i]=dp[i+1]
                if s[i]==t[j]:
                    dp[i]+=diag

                diag=temp
        return dp[0]

        