class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        fuel = 0 
        l,r = 0,0
        while l < len(gas):
            fuel += gas[r % len(gas)] - cost[r % len(gas)]
            if fuel < 0:
                fuel = 0
                r += 1 
                l = r 
            else:
                r += 1
                if l == r % len(gas):
                    return l 
        
        return -1


    
        