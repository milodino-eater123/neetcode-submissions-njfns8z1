from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for x in range(len(nums)+1)]
        hmap=defaultdict(int)
        for n in nums:
            hmap[n]+=1
        
        for key,value in hmap.items():
            freq[value].append(key)
        
        res = []

        for num in freq[::-1]:
            for n in num:
                res.append(n)
                if len(res)==k:
                    return res


    
    

        