from heapq import heappop, heappush
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        dp = {}
        minHeap = []
        #sort intervals, sort queries

        #for each query, add all intervals such that start<query
        #if end<query, pop permanently
        i = 0
        intervals.sort()
        queries1=sorted(queries)
        for q in queries1:
            while i<len(intervals) and intervals[i][0] <= q:
                start,end = intervals[i][0],intervals[i][1]
                heappush(minHeap,(end-start+1,end))
                i += 1
            while minHeap:
                length,end = minHeap[0]
                if end<q:
                    heappop(minHeap)
                else:
                    break
            dp[q] = minHeap[0][0] if minHeap else -1 
        
        return [dp[x] for x in queries]





        