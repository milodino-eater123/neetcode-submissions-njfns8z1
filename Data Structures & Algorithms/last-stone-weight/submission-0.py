from heapq import heapify,heappush,heappop
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapify(stones)
        while len(stones) > 1:
            first,second = -heappop(stones),-heappop(stones)
            diff = first - second
            if diff > 0:
                heappush(stones,-diff)
        
        if stones:
            return -stones[0]
        else:
            return 0

        