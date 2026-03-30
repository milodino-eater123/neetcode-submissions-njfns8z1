class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def timeTaken(speed):
            time = 0
            for bananas in piles:
                time += math.ceil(bananas/speed)
            
            return time

        low,high = 1,max(piles)
        while high > low:
            mid = (high+low)//2
            if timeTaken(mid) <= h:
                high = mid
            else:
                low = mid + 1 

        return low

        