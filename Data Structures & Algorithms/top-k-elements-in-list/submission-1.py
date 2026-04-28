from collections import defaultdict
from heapq import heappush,heappop
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = defaultdict(int)
        for n in nums:
            hmap[n]+=1
        
        minHeap = []
        for key,value in hmap.items():
            heappush(minHeap,(value,key))

            if len(minHeap)>k:
                heappop(minHeap)
        
        return [x[1] for x in minHeap]


        