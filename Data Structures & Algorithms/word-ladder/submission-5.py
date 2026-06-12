class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        level,count = {beginWord},1
        wordList = set(wordList)
        while level:
            if endWord in level:
                return count
            count+=1
            newLevel = set()
            for word in level:
                for i in range(len(word)):
                    for j in range(0,27):
                        x = chr(ord("a")+j)
                        new = word[:i]+x+word[i+1:]
                        if new in wordList:
                            newLevel.add(new)
                            wordList.remove(new)
            level=newLevel
        return 0


        