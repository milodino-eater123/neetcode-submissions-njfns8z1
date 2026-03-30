class Solution:
    def rob(self, nums: List[int]) -> int:
        #max at i is i-1 or i-2 + i
        prev2 = 0
        prev1 = 0
        for i in range(0,len(nums)):
            temp = prev1
            prev1 = max(prev1,prev2+nums[i])
            prev2 = temp
        

        return prev1
        