class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        res = False
        wordDict = set(wordDict)
        hset = set()
        def dfs(i,string):
            nonlocal res,hset
            if (i,string) in hset:
                return
            if i >= len(s):
                if string in wordDict:
                    res = True
                return
        
            c = s[i]
            
            hset.add((i,string))
            dfs(i+1,string+c)

            if string in wordDict:
                dfs(i+1,c)


        dfs(0,"")
        return res
        