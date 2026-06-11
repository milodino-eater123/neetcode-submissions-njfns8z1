class Solution:
    def jump(self, nums: List[int]) -> int:
        curRange,newRange,res = 0,0,0
        for i,n in enumerate(nums):
            if i>curRange:
                curRange=newRange
                res+=1
            newRange = max(newRange,i+n)
        return res

        