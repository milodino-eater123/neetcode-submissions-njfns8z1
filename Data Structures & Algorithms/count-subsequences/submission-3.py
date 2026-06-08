class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        l1,l2=len(s),len(t)
        dp = [0 for _ in range(l2)]
        for i in range(l1-1,-1,-1):
            prev=1
            for j in range(l2-1,-1,-1):
                temp=dp[j]
                if s[i]==t[j]:
                    dp[j]+=prev
                prev = temp
        return dp[0]

                


        