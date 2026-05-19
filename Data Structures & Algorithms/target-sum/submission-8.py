from collections import defaultdict
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[0]=1
        for i in range(len(nums)):
            newDP = defaultdict(int)
            for key,value in dp.items():
                
                newDP[key+nums[i]]+=dp[key]
                newDP[key-nums[i]]+=dp[key]
            dp = newDP
        
        return dp[target]