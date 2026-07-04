class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        for l in range(1,n+1):
            for i in range(n-l+1):
                dp[i][i+l-1] = (l==1) or (s[i]==s[i+l-1] and (dp[i+1][i+l-2] or l==2))
        def par(i):
            if i>=n:
                return [[]]
            res = []
            for j in range(i,n):
                if dp[i][j]:
                    for part in par(j+1):
                        whole = [s[i:j+1]] + part
                        res.append(whole)
            return res
        return par(0)
         