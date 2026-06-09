"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from heapq import heappush,heappop
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        res,minHeap=1,[0]
        intervals.sort(key=lambda x:x.start)
        for intv in intervals:
            minEnd=minHeap[0]
            if intv.start<minEnd:
                res += 1
            else:
                heappop(minHeap)
            heappush(minHeap,intv.end)
        return res

        