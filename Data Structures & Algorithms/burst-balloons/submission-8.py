class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        hmap = {}
        def dfs(total,avail):
            if tuple(avail) in hmap:
                return hmap[tuple(avail)]
            best =0
            for i,n in enumerate(avail):
                prev = avail[i-1] if i-1>=0 else 1
                next = avail[i+1] if i+1<len(avail) else 1
                n*=prev*next
                best = max(best,n+dfs(total+n,avail[:i]+avail[i+1:]))
            hmap[tuple(avail)]=best
            return best       
        return dfs(0,nums)
        