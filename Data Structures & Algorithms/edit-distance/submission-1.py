class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        #find longest consecutive subsring
        #find how many letters match(i.e. can be replaced)
        #other letters, delete
        res = float('inf')
        def dfs(i,j,edits,lastMatch):
            nonlocal res
            if i >= len(word1) and j >= len(word2):
                diff1 = i - lastMatch[0] - 1 
                diff2 = j - lastMatch[1] - 1
                total = max(diff1,diff2)
                res = min(res,edits+total)
                return
            
            if i < len(word1):
                dfs(i+1,j,edits,lastMatch)
            if j < len(word2):
                dfs(i,j+1,edits,lastMatch)

            if i<len(word1) and j<len(word2) and word1[i] == word2[j]:
                diff1 = i - lastMatch[0] - 1 
                diff2 = j - lastMatch[1] - 1
                total = max(diff1,diff2)
                dfs(i+1,j+1,edits+total,(i,j))            

        dfs(0,0,0,(-1,-1))
        return res

