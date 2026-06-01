class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp ={0:0}
        coins.sort()
        for i in range(1,amount+1):
            dp[i]=float('inf')
            for c in coins:
                if c>i:
                    break
                dp[i] = min(dp[i],1+dp[i-c])
        return dp[amount] if dp[amount]!=float('inf') else -1
        

        


    
        

        