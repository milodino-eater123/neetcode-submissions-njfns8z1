class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        def dfs(choices):
            
            maxCoins = 0
            for i in range(len(choices)):
                before = choices[i-1] if i-1>=0 else 1
                cur = choices[i]
                after = choices[i+1] if i+1<len(choices) else 1 
                coins = before*cur*after + dfs(choices[:i]+choices[i+1:])
                maxCoins = max(maxCoins,coins)
            
            return maxCoins
        return dfs(nums)
        