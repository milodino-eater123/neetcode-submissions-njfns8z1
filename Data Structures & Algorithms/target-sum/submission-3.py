from collections import defaultdict
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[nums[0]] += 1 
        dp[-nums[0]] += 1 

        for i in range(1,len(nums)):
            new_dp = defaultdict(int)
            for key,value in dp.items():
                new_dp[key+nums[i]] += value
                new_dp[key-nums[i]] += value
            dp = new_dp
        
        return dp[target]


        