class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = 0
        stations=0
        fuel = 0
    
        for i in range(2):
          for i in range(len(gas)):
            g=gas[i]
            c=cost[i]
            fuel += g
            if fuel<c:
                start = i+1
                stations = 0
                fuel = 0
            else:
                stations+=1
                fuel-=c
        print(stations)
        return start if stations>=len(gas) else -1
            
        