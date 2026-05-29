import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def time(speed):
            res = 0
            for p in piles:
                time = math.ceil(p/speed)
                res += time
            return res
        
        low,high=1,max(piles)

        while high>low:
            mid = (low+high)//2
            if time(mid) <= h:
                high=mid
            else:
                low=mid+1
        
        return low
                
        