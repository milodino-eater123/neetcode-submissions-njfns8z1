from heapq import heappush,heappop
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []
        for s in stones:
            heappush(maxHeap,-s)
        
        while len(maxHeap) > 1:
            y = -heappop(maxHeap)
            x = -heappop(maxHeap)

            new = y-x
            if new:
                heappush(maxHeap,-new)
        
        return -maxHeap[0] if maxHeap else 0


        