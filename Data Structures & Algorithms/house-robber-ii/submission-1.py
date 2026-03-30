class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        prev1,prev2 = 0,0
        for i in range(0,len(nums)-1):
            temp = prev1
            prev1 = max(prev1,prev2+nums[i])
            prev2 = temp
        
        ans1 = prev1
        
        prev1,prev2 = 0,0
        for i in range(1,len(nums)):
            temp = prev1
            prev1 = max(prev1,prev2+nums[i])
            prev2 = temp
        
        return max(ans1,prev1)
            
        
