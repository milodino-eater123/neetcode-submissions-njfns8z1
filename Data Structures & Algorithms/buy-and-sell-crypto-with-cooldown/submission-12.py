class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #0,1,2 = no stock,stock,cooldown
        dp = [0,float("-inf"),float("-inf")]

        for i,p in enumerate(prices):
            newDP = [0]*3
            newDP[0]=max(dp[0],dp[2])
            newDP[1]=max(dp[0]-p,dp[1])
            newDP[2]=dp[1]+p
            dp=newDP
        
        return max(dp)
        