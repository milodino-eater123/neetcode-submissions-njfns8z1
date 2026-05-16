class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        dp[0] = 0
        for i in range(1,amount+1):
            dp[i] = float('inf')
            for c in coins:
                if i-c < 0:
                    continue
                if dp[i-c] != -1:
                    dp[i] = min(dp[i],dp[i-c]+1)
            dp[i] = -1 if dp[i]==float('inf') else dp[i]
        
        return dp[amount]
                

    
        

        