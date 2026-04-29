class Solution:
    def trap(self, height: List[int]) -> int:
        fromLeft = {}

        maxBar = 0
        for i,h in enumerate(height):
            fromLeft[i] = maxBar
            maxBar = max(maxBar,h)
        
        res = 0

        maxBar = 0
        for i in range(len(height)-1,-1,-1):
            h = height[i]
            lowerBar = min(maxBar,fromLeft[i])
            if h < lowerBar:
                res += (lowerBar-h)
            
            maxBar = max(maxBar,h)
        
        return res

        