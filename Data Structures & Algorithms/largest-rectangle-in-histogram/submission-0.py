class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        def push(lst,tupl):
            val = tupl[1]
            while lst and lst[-1][1] >= val:
                tupl = (lst[-1][0],tupl[1])
                lst.pop()
            lst.append(tupl)

        
        res = 0
        stack = []
        
        for i,val in enumerate(heights):
            push(stack,(i,val))
            for j,val1 in stack:
                width = i - j + 1
                height = min(val1,val)
                res = max(res,width*height)
        
        return res
            

        