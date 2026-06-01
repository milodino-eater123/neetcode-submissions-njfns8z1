class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax,curMin,res=1,1,float("-inf")
        for n in nums:
            new1,new2 = curMax*n,curMin*n
            curMax=max(new1,new2,n)
            curMin=min(new1,new2,n)
            res = max(res,curMax)   
        return res
        