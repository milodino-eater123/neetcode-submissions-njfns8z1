"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals.sort(key = lambda x: x.start)
        
        theEnd = intervals[0].end
        for obj in intervals[1:]:
            start = obj.start
            end = obj.end
            if theEnd > start:
                return False
            else:
                theEnd = end
        return True
        

