class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = fuel = i = 0
        while i < (2*len(gas)):
            j = i%len(gas)
            fuel += gas[j]
            if fuel < cost[j]:
                start = i + 1 
                fuel = 0
            else:
                fuel-=cost[j]
            i += 1
        
        return start if start<len(gas) else -1


        
        