class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def dfs(i,j):
            if i>= len(s) and j>=len(p):
                return True
            if i>=len(s) and j==len(p)-2 and p[j+1] == "*":
                return True
            if i>= len(s) or j >= len(p):
                return False
            #"n*"
            if j+1<len(p) and p[j+1] == "*":
                dontUse = dfs(i,j+2)
                use = (p[j] == "." or p[j] == s[i]) and dfs(i+1,j)
                return use or dontUse
            
            elif p[j] == "." or p[j] == s[i]:
                return dfs(i+1,j+1)
            else:
                return False
        
        return dfs(0,0)