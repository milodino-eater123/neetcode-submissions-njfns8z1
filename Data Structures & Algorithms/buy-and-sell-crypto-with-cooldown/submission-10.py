class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #0,1,2 = canBuy,canSell,wait
        dp = [0,float("-inf"),0]
        for i in range(len(prices)):
            newDP = [0]*3
            newDP[0]=max(dp[0],dp[2])
            newDP[1]=max(dp[0]-prices[i],dp[1])
            newDP[2]=dp[1]+prices[i]
            dp = newDP
            print(i,prices[i],dp)
        
        return max(dp)
        




        