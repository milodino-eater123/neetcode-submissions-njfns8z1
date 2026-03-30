class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        hmap = {}
        def build(i,curSum):
            nonlocal hmap
            if (i,curSum) in hmap:
                return hmap[(i,curSum)]
            if i >= len(nums):
                if curSum == target:
                    return 1
                return 0
            
            n = nums[i]
            
            suhm = build(i+1,curSum+n) + build(i+1,curSum-n)
            hmap[(i,curSum)] = suhm
            return suhm
       
        
        return build(0,0)
        
        