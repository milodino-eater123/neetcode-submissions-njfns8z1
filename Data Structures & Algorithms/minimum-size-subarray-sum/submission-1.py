class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        suhm = 0
        res = float('inf')
        
        for r in range(0,len(nums)):
            suhm += nums[r]
            #shrink condition
            while suhm >= target:
                res = min(res,r-l+1)
                suhm -= nums[l]
                l += 1 
            r += 1 

        
        return 0 if res == float('inf') else res