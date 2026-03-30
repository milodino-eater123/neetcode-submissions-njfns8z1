
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        hmap = {}
        def dfs(i,canBuy,mustWait):
            nonlocal res,hmap
            if (i,canBuy,mustWait) in hmap:
                return hmap[(i,canBuy,mustWait)]
            if i>=len(prices):
                return 0
            #do nothing
            nothing = dfs(i+1,canBuy,False) # same as prev

            #buy          
            buy = -prices[i] + dfs(i+1,False,False) if canBuy and not mustWait else float("-inf")
            #sell
            sell = prices[i]+ dfs(i+1,True,True) if not canBuy and not mustWait else float("-inf")

            best = max(nothing,buy,sell)
            hmap[(i,canBuy,mustWait)] = best
            return best
            

        return dfs(0,True,False)
      


        #counter for buy is always 2
        #after buying, counter = 0 , 
        #after selling, counter += 1  







        