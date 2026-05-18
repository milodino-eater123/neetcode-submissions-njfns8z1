class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2==1:
            return False

        dp = {0}
        target = sum(nums)/2
        for i in range(len(nums)):
            newDP = set()
            for total in dp:
                newDP.add(total)
                if total+nums[i]==target:
                    return True
                if total+nums[i]<target:
                    newDP.add(total+nums[i])
            dp = newDP
        
        return False