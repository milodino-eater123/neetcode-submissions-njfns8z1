class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        curLevelWords = {beginWord}
        res = 0
        wordList = set(wordList)
        while curLevelWords:
            res += 1 
            if endWord in curLevelWords:
                return res
            newLevel = set()
            for word2 in wordList.copy():
                for word1 in curLevelWords:
                    similarity=0
                    for i in range(len(word1)):
                        if word1[i]==word2[i]:
                            similarity+=1
                    if similarity==len(word1)-1:
                        newLevel.add(word2)
                        wordList.discard(word2)
            curLevelWords=newLevel
        
        return 0




            
        
                    


        