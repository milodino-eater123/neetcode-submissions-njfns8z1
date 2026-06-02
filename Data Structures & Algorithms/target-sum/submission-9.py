from collections import defaultdict
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        dp[0]=1
        for n in nums:
            newDP=defaultdict(int)
            for key,value in dp.items():
                newDP[key+n]+=value
                newDP[key-n]+=value
            dp=newDP
        return dp[target]


        