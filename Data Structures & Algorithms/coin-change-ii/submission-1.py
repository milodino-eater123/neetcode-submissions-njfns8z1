class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        hmap = {}
        def dfs(i,curSum):
            if (i,curSum) in hmap:
                return hmap[(i,curSum)]
            if curSum > amount:
                return 0 
            if i >= len(coins):
                if curSum == amount:
                    return 1
                return 0 
            use = dfs(i,curSum+coins[i])
            dontUse = dfs(i+1,curSum)
            hmap[(i,curSum)] = use+dontUse
            return use + dontUse

        return dfs(0,0)
        