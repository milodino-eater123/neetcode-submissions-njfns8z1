class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res,curEnd = 0,intervals[0][1]
        for i in range(1,len(intervals)):
            start,end = intervals[i]
            if start>=curEnd:
                curEnd=end
            else:
                res+=1
                curEnd=min(curEnd,end)
        return res
        