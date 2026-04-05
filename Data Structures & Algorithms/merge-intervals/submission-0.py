class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()
        curStart,curEnd = intervals[0]
        for i in range(1,len(intervals)):
            if intervals[i][0] <= curEnd:
                curEnd = max(curEnd,intervals[i][1])
            else:
                res.append([curStart,curEnd,])
                curStart,curEnd = intervals[i]
        res.append([curStart,curEnd])
        return res


        