class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        #initialise
        dic = collections.defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                new = word[:i]+"*"+word[i+1:]
                dic[new].append(word)
        start,end = [beginWord],[endWord]
        res = 0
        visited1,visited2 = {beginWord},{endWord}
        while start and end:
            temp = []
            if len(start)<=len(end):
                while start:
                    word = start.pop()
                    if word in visited2:
                        return res +1
                    for i in range(len(word)):
                        new = word[:i]+"*"+word[i+1:]
                        for child in dic[new]:
                            if child not in visited1:
                                temp.append(child)
                                visited1.add(child)
                start=temp
            else:
                while end:
                    word=end.pop()
                    if word in visited1:
                        return res+1
                    for i in range(len(word)):
                        new = word[:i]+"*"+word[i+1:]
                        for child in dic[new]:
                            if child not in visited2:
                                temp.append(child)
                                visited2.add(child)
                end=temp
            res += 1
            
        return 0

                    
                


        