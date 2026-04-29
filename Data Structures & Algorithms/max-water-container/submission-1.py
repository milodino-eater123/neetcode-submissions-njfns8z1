class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l,r = 0,len(heights)-1
        while r>l:
            h = min(heights[r],heights[l])
            w = r - l
            area = h * w
            res = max(res,area)

            if heights[r]<heights[l]:
                r -= 1
            else:
                l += 1
        
        return res
        

       


        