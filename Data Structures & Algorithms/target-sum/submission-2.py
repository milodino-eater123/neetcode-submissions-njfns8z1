from collections import defaultdict
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = [defaultdict(int) for _ in range(len(nums))]
        dp[0][nums[0]] += 1 
        dp[0][-nums[0]] += 1 

        for i in range(1,len(nums)):
            for key,value in dp[i-1].items():
                dp[i][key+nums[i]] += value
                dp[i][key-nums[i]] += value
        
        return dp[len(nums)-1][target]


        