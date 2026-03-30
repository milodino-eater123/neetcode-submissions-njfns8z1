class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = r = 0
        suhm = 0
        res = float('inf')
        while True:
            if r >= len(nums):
                break
            #expand until valid
            while r < len(nums) and suhm < target:
                suhm += nums[r]
                r += 1 
            if suhm < target:
                break
            #shrink
            while True:
                if suhm - nums[l] >= target:
                    suhm -= nums[l]
                    l += 1 
                else:
                    break

            if r - l < res:
                res = r - l 

            #remove 1 number from window
            suhm -= nums[l]
            l += 1 
        if res == float('inf'):
            return 0
        return res

