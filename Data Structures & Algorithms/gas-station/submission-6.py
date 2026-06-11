class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):
            return -1
        res,fuel = 0,0
        for i in range(len(gas)):
            net = gas[i]-cost[i]+fuel
            if net<0:
                res = i+1
                fuel=0
            else:
                fuel = net
        return res
            
        