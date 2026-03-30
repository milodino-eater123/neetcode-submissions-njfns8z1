from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0]*(amount+1) for _ in range(len(coins)+1)]
        for thing in dp:
            thing[-1] = 1 
        
        for j in range(len(coins)-1,-1,-1):
            for curSum in range(amount-1,-1,-1):
                if curSum + coins[j] > amount:
                    dp[j][curSum] = dp[j+1][curSum]
                else:
                    dp[j][curSum] = dp[j][curSum+coins[j]] + dp[j+1][curSum]
        
        for row in dp:
            print(row)
        return dp[0][0]

sol = Solution()
print(sol.change(5, [1,2,5]))



        


        