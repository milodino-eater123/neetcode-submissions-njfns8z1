from collections import defaultdict
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        hmap = {}
        def dfs(i,total):
            if (i,total) in hmap:
                return hmap[(i,total)]
            if total==amount:
                return 1
            if i==len(coins):
                return 0

            ways = 0
            if total + coins[i] <= amount:
                ways += dfs(i,total+coins[i])
                ways += dfs(i+1,total)
            hmap[(i,total)]=ways
            return ways
        
        return dfs(0,0)
            
        


        