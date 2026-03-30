class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = float('-inf')
        minVal,maxVal = 1,1
        for n in nums:
            maxVal *= n
            minVal *= n
            temp = maxVal
            maxVal=max(maxVal,minVal,n)
            minVal=min(minVal,temp,n)
            res = max(res,maxVal)
        return res
            