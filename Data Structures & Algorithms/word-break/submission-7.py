class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        index,wordDict = [-1],set(wordDict)
        for i in range(len(s)):
            for j in index:
                if s[j+1:i+1] in wordDict:
                    index.append(i)
                    break
        return index[-1]==len(s)-1

        

        
        