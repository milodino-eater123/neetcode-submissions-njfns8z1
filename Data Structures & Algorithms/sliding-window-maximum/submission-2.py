from heapq import heappush,heappop
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []

        #construct sliding window and max heap
        heap = []
        for i in range(0,k):
            heappush(heap,-nums[i])
        res.append(-heap[0])

        #move sliding window
        removed = []
        l,r = 0,k-1
        while r+1 < len(nums):
            #shrink
            heappush(removed,-nums[l])
            l += 1 

            #expand
            heappush(heap,-nums[r+1])
            r += 1

            #find new max
            while removed and heap[0] == removed[0]:
                heappop(heap)
                heappop(removed)
                
            res.append(-heap[0])

        return res
            


        

        