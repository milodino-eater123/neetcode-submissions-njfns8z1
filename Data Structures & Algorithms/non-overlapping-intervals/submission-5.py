from heapq import heappush, heappop
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        curEnd = intervals[0][1]
        for i in range(1,len(intervals)):
            if intervals[i][0] < curEnd:
                if intervals[i][1] < curEnd:
                    curEnd = intervals[i][1]
                res += 1
            else:
                curEnd = intervals[i][1]
        return res





