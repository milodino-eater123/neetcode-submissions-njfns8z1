class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res,cur = [],intervals[0]
        for i in range(1,len(intervals)):
            start,end = intervals[i]
            if start>cur[1]:
                res.append(cur)
                cur=intervals[i]
            else:
                cur = [cur[0],max(end,cur[1])]
        return res + [cur]