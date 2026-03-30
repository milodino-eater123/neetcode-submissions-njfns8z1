class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        hmap = {}
        def dfs(i,canBuy):
            if (i,canBuy) in hmap:
                return hmap[(i,canBuy)]
            if i >= len(prices):
                return 0
            
            wait = dfs(i+1,canBuy)
            
            buy = -prices[i] + dfs(i+1,False) if canBuy else float("-inf")
                
            
            sell = prices[i] + dfs(i+2,True) if not canBuy else float("-inf")
                
            best = max(buy,sell,wait)
            hmap[i,canBuy] = best
            return best
        return dfs(0,True)
    
            



        