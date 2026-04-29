class Solution:
    def trap(self, height: List[int]) -> int:
        l,r=0,len(height)-1
        leftBar,rightBar=0,0
        res = 0

        while r>=l:
            if leftBar < rightBar:
                if leftBar>height[l]:
                    res += (leftBar-height[l])
                leftBar = max(leftBar,height[l])       
                l += 1
            
            else:
                if rightBar>height[r]:
                    res += (rightBar-height[r])
                rightBar = max(rightBar,height[r])
                r -= 1
        
        return res


        