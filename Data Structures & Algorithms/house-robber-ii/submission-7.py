class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]

        return max(self.rob1(nums[:-1]),self.rob1(nums[1:]))
    

    def rob1(self, nums: List[int]) -> int:
        prev1,prev2 = nums[0],0
        for i in range(1,len(nums)):
            temp = prev1
            prev1 = max(prev1,prev2+nums[i])
            prev2 = temp   
        return prev1
        