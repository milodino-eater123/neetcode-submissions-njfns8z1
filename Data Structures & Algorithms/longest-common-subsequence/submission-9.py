class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n,m=len(text1),len(text2)
        if n<m:
            n,m,text1,text2=m,n,text2,text1
        dp=[0]*(m+1)
        for i in range(n):
            prev=0
            for j in range(m):
                temp=dp[j]
                if text1[i]==text2[j]:
                    dp[j]=1+prev
                else:
                    dp[j]=max(dp[j],dp[j-1])
                prev=temp
        return dp[-2]
            
        