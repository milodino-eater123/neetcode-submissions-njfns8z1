from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lst = []
        nums = set(nums)
        for n in nums:
            if n-1 not in nums:
                lst.append(n)
        
        max_seq = 0

        for n in lst:
            i = n
            counter = 0
            while i in nums:
                counter += 1 
                max_seq = max(max_seq,counter)
                i += 1 

        return max_seq

