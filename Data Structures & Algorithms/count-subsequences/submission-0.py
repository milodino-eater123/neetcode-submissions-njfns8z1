class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        hmap = {}
        def dfs(i,j):
            if (i,j) in hmap:
                return hmap[(i,j)]
            if j >= len(t):
                return 1
            if i >= len(s):
                return 0
            
            dontUse = dfs(i+1,j)

            use = dfs(i+1,j+1) if s[i] == t[j] else 0

            hmap[(i,j)] = dontUse + use

            return dontUse + use
        
        return dfs(0,0)

        