class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        res,length = "",0
        dp = [[False]*n for _ in range(n)]
        for l in range(1,n+1):
            for i in range(0,n-l+1):
                dp[i][i+l-1] = l==1 or (s[i]==s[i+l-1] and (l==2 or dp[i+1][i+l-2]))
                if dp[i][i+l-1] and l>length:
                    res = s[i:i+l]
                    length=l
                    
        return res
        