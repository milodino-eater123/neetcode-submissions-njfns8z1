from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0]*(amount+1)
        dp[-1] = 1 
        for j in range(len(coins)-1,-1,-1):
            newDP = [0] * (amount+1)
            newDP[-1] = 1
            for curSum in range(amount-1,-1,-1):
                if curSum + coins[j] > amount:
                    newDP[curSum] = dp[curSum]
                else:
                    newDP[curSum] = newDP[curSum+coins[j]] + dp[curSum]
            dp = newDP

        return dp[0]



        


        