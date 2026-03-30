class Solution:
    def rob(self, nums: List[int]) -> int:
        #max at i is i-1 or i-2 + i
        if len(nums) == 1:
            return nums[0]
        prev2 = nums[0]
        prev1 = max(nums[0],nums[1])
        for i in range(2,len(nums)):
            temp = prev1
            prev1 = max(prev1,prev2+nums[i])
            prev2 = temp
        

        return prev1
        