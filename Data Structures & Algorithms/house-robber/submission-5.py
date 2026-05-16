class Solution:
    def rob(self, nums: List[int]) -> int:
        prev1,prev2 = nums[0],0

        for i in range(1,len(nums)):
            temp = prev1
            prev1 = max(prev1,prev2+nums[i])
            prev2 = temp
        
        return prev1
        