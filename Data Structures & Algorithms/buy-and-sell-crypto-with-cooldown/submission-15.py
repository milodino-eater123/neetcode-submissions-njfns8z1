class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0,float("-inf"),float("-inf")]
        for p in prices:
            newDP = [0]*3
            newDP[0] = max(dp[0],dp[2])
            newDP[1] = max(dp[1],dp[0]-p)
            newDP[2] = dp[1]+p
            dp = newDP
        return max(dp)
        