class Solution:
    def maxArea(self, heights: List[int]) -> int:

        #two pointers, no need for storage of data btwn pointers
        
        #start from ends

        #only way to get more water, if the lower one can move to a higher one

        #iterate lower one down until you find a higher one, log value, then repeat until l=r
        #-> On, visit each bar once max

        l,r = 0, len(heights) - 1 
        res = 0
        while r > l:
            if heights[l] <= heights[r]:
                res = max(res, (r-l)*heights[l])
                l += 1 
            else:
                res = max(res, (r-l)*heights[r])
                r -= 1 

        return res




        