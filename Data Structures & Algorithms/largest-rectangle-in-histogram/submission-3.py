class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        left = [-1]*(len(heights))
        right = [len(heights)]*(len(heights))

        stack1,stack2=[],[]

        for i in range(len(heights)):
            h=heights[i]
            while stack1 and heights[stack1[-1]]>h:
                j = stack1.pop()
                right[j]=i
            stack1.append(i)
        
        for i in range(len(heights)-1,-1,-1):
            h=heights[i]
            while stack2 and heights[stack2[-1]]>h:
                j=stack2.pop()
                left[j]=i
            stack2.append(i)
        
        res = 0
        for i,h in enumerate(heights):
            length = right[i]-left[i]-1
            res = max(res,(length*h))

        return res

        