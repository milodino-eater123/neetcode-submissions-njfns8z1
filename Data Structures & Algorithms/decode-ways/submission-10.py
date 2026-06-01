class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {}
        dp[-1]=1
        for i,c in enumerate(s):
            if c == "0":
                if i-1>=0 and s[i-1]=="1" or s[i-1]=="2":
                    dp[i]=dp[i-2]
                else:
                    return 0      
            elif i-1>=0 and 11<=int(s[i-1:i+1])<=26:
                dp[i]=dp[i-1]+dp[i-2]
            else:
                dp[i]=dp[i-1]
        return dp[len(s)-1]

        