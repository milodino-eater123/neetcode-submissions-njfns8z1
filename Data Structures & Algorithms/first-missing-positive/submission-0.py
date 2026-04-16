class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        res = 0
        nums.sort()
        for n in nums:
            if n <= 0:
                continue
            if n > res + 1:
                return res +1
            else:
                res = n
        return res + 1
        
        [1,1,2,3,4,5,6]