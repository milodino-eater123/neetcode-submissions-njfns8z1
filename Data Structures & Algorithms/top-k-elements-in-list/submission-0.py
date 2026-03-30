from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #input [1,2,2,3,3,3]
        hmap = {}
        # -> hmap
        for n in nums:
            hmap[n] = hmap.get(n,0) + 1 

        # -> freq list of preset length, O(1) insertion
        freq_list = [[] for i in range(len(nums) + 1)]
        for num,freq in hmap.items():
            freq_list[freq].append(num)

        #parse freq list
        res = []
        for i in range(len(nums),0,-1):
            nums = freq_list[i]
            for n in nums:
                res.append(n)
                if len(res) == k:
                    return res
                

        

        
        