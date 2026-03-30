"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

from collections import defaultdict
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        meetings = 0
        res = 0
        dic = defaultdict(int)
        for x in intervals:
            dic[x.start] += 1 
            dic[x.end] -= 1
        
        for key in sorted(dic.keys()):
            meetings += dic[key]
            res = max(res,meetings)
        
        return res

        