from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        nums_set = set(nums)

        for n in nums:
            if n-1 in nums_set:
                continue
            count = 1
            while n+1 in nums_set:
                count += 1
                n+=1
            res = max(res,count)
        
        return res
            
            
            
        
