from heapq import heapify,heappush,heappop
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        heapify(nums)
        self.heap = nums
        while len(self.heap) > k:
            heappop(self.heap)
        
    def add(self, val: int) -> int:
        heappush(self.heap,val)
        if len(self.heap) > self.k:
            heappop(self.heap)
        return self.heap[0]
        
