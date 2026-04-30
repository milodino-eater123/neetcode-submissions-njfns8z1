class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #l is lowest price found so far

        #r is basically any point

        res = 0
        l = 0
        for i,p in enumerate(prices):
            if p >= prices[l]:
                profit = p - prices[l]
                res = max(res,profit)
            else:
                l = i
        
        return res

        