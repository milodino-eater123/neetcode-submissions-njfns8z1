class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n,m = len(text1),len(text2)
        if n<m:
            n,m=m,n
            text1,text2=text2,text1
        dp = [0]*(m+1)
        for i in range(n):
            newDP = [0]*(m+1)
            for j in range(m):
                newDP[j]=max(dp[j],newDP[j-1])
                if text1[i]==text2[j]:
                    newDP[j]=1+dp[j-1]
            dp=newDP
        return dp[-2]

        