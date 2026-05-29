class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        originalReach = nums[0]
        newReach = 0
        res = 0
        for i,n in enumerate(nums):
            if i>originalReach:
                res += 1
                originalReach=newReach
            newReach = max(newReach,i+n)
            if originalReach >= len(nums)-1:
                return res + 1
            
        