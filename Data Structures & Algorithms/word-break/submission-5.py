class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        index = [-1]
        wordDict = set(wordDict)
        for i in range(len(s)):
            flag = False
            for j in index:
                if s[j+1:i+1] in wordDict:
                    flag = True
                    break
            if flag:
                index.append(i)
        return index[-1]==len(s)-1

        

        
        