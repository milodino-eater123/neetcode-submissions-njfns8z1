from heapq import heappush, heappop
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        sorted_q=sorted(queries)
        intervals.sort()
        i,minHeap,hmap=0,[],{}
        for q in sorted_q:
            while i<len(intervals) and intervals[i][0]<=q:
                heappush(minHeap,(intervals[i][1]-intervals[i][0],intervals[i][1]))
                i+=1
            while minHeap and minHeap[0][1]<q:
                heappop(minHeap)
            hmap[q]=minHeap[0][0]+1 if minHeap else -1
        return [hmap[q] for q in queries]
            
        