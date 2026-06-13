from heapq import heappush,heappop
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        ori,hmap,intervals,queries = queries,{},sorted(intervals),sorted(queries)
        minHeap,i = [],0
        for q in queries:
            while i<len(intervals) and intervals[i][0]<=q:
                heappush(minHeap,(intervals[i][1]-intervals[i][0]+1,intervals[i][1]))
                i+=1
            while minHeap and minHeap[0][1]<q:
                heappop(minHeap)
            hmap[q]=minHeap[0][0] if minHeap else -1
        print(hmap)
        return [hmap[q] for q in ori]


        