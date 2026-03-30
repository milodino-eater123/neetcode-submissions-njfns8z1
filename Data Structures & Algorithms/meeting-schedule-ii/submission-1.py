"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key = lambda x: x.start)
         
        room_ends = [intervals[0].end]
        counter = 1

        for interval in intervals[1:]:
            start = interval.start
            end = interval.end
            if room_ends[0] > start:
                counter += 1
                heapq.heappush(room_ends,end)
            else:
                heapq.heappop(room_ends)
                heapq.heappush(room_ends,end)
        return counter
                
            



        
        
        