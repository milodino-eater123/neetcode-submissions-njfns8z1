import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        low,high = 1,max(piles)

        def time(speed):
            output = 0
            for p in piles:
                output += math.ceil(p/speed)
            return output

        while high > low:
            mid = (high+low)//2
            if time(mid) > h:
                low = mid + 1 
            elif time(mid) <= h:
                high = mid
        
        return low

            


        