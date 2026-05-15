class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = 0
        stations=0
        fuel = 0
    
        for x in range(2):
          for i in range(len(gas)):
            fuel += gas[i]
            #choice 1: reset
            if fuel<cost[i]:
                start = i+1
                stations = 0
                fuel = 0
            #choice 2: continue
            else:
                stations+=1
                fuel-=cost[i]

        return start if stations>=len(gas) else -1
            
        
        