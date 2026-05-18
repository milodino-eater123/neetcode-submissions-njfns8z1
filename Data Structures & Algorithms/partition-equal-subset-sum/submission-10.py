class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2==1:
            return False

        dp = {0:True}
        target = sum(nums)/2
        for i in range(len(nums)):
            newDP = {}
            for key,value in dp.items():
                newDP[key]=value
                if key+nums[i]<=target:
                    newDP[key+nums[i]]=True
            dp = newDP
        
        return target in dp