from collections import defaultdict
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {(0,True):0}
        res = 0
        while dp:
            newDP = defaultdict(lambda: float('-inf'))
            for key,value in dp.items():
                j, canBuy = key
                curSum = value
                if j >= len(prices):
                    res = max(res,curSum)
                    continue
                newDP[(j+1,canBuy)]= max(newDP[(j+1,canBuy)],value)
                if canBuy:
                    newDP[(j+1,False)] = max(newDP[(j+1,False)],value - prices[j])
                else:
                    newDP[(j+2,True)] = max(newDP[(j+2,True)],value + prices[j])
            dp = newDP

        return res



        