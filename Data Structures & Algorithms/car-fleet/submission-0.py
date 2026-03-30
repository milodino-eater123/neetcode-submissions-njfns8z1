class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(zip(position,speed))

        fleets = len(position)
        nextTime = -1
      
        #iterate from back of pos
        for i in range(len(speed)-1,-1,-1):
           pos = pairs[i][0]
           speed = pairs[i][1]
           curTime = (target - pos) / speed
           if curTime > nextTime:
               nextTime = curTime
           else:
               fleets -= 1 


        return fleets
        #time taken for i to reach
        #if prev has <= time taken, add, if not counter += 1,time taken = prev
        #prev prev has <= time taken,add

        