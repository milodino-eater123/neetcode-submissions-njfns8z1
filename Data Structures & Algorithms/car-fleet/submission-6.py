class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = len(position)
        both = sorted(zip(position,speed))
        nextTime = (target-both[-1][0])/both[-1][1]
        for i in range(len(both)-2,-1,-1):
            p,s = both[i]
            curTime = (target-p)/s
            if curTime <= nextTime:
                res -= 1
            else:
                nextTime = curTime
        return res


        