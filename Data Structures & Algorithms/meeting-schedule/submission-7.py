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
        intervals.sort(key=lambda x:x.start)
        cur=intervals[0]
        for intv in intervals[1:]:
            start,end = intv.start,intv.end
            if start<cur.end:
                return False
            else:
                cur=intv
        return True


