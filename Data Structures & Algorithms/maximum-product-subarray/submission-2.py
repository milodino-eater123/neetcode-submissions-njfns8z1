class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minVal,maxVal = 1,1
        res = float('-inf')

        for n in nums:
            new = n
            useMin = n*minVal
            useMax = n*maxVal
            maxVal = max(new,useMin,useMax)
            minVal = min(new,useMin,useMax)
            res = max(res,maxVal)
        
        return res
        
        