class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        hmap = {}
        def dfs(i,j):
            nonlocal hmap
            if (i,j) in hmap:
                return hmap[(i,j)]
            if i>=len(text1) or j>=len(text2):
                return 0
            


            if text1[i] == text2[j]:
                value = 1 + dfs(i+1,j+1)
            else:
                value = max(dfs(i+1,j),dfs(i,j+1))
            
            hmap[(i,j)] = value
            return value
        return dfs(0,0)


        