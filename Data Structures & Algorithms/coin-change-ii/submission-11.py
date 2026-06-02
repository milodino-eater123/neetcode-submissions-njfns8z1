class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0]*(amount+1)
        dp[0]=1
        for i,c in enumerate(coins):
            for j in range(1,amount+1):
                if j-c<0:
                    continue
                dp[j]+=dp[j-c]
        return dp[amount]