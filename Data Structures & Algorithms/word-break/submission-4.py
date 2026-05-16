class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        starts = {0}
        wordDict = set(wordDict)
        for i,c in enumerate(s):
            for j in starts:
                if s[j:i+1] in wordDict:
                    starts.add(i+1)
                    break
        
        return max(starts) == len(s)

        
        