class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)
        fromLeft,stack = [-1]*n,[]
        for i in range(n-1,-1,-1):
            while stack and heights[stack[-1]]>heights[i]:
                j = stack.pop()
                fromLeft[j]=i
            stack.append(i)
        res,stack = 0,[]
        for i in range(n):
            while stack and heights[stack[-1]]>heights[i]:
                j = stack.pop()
                res = max(res,heights[j]*(i-fromLeft[j]-1))
            stack.append(i)
        for j in stack:
            res = max(res,heights[j]*(n-fromLeft[j]-1))
        return res

        