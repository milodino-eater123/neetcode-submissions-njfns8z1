class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        res = 0
        def build(i,curSum):
            nonlocal res
            if i >= len(nums):
                if curSum == target:
                    res += 1
                return
            
            n = nums[i]
            
            build(i+1,curSum+n)

            build(i+1,curSum-n)
       
        
        build(0,0)
        return res
        