class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stack = [(0,0,True)]
        res = 0
        while stack:
            newStack = set()
            while stack:
                i,curSum,canBuy = stack.pop()
                if i >= len(prices):
                    res = max(res,curSum)
                    continue
                newStack.add((i+1,curSum,canBuy))
                if canBuy:
                    newStack.add((i+1,curSum-prices[i],False)) 
                else:
                    newStack.add((i+2,curSum+prices[i],True))
            stack = list(newStack)
        
        return res



        