class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        dic = collections.defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                mod = word[:i] + "*" + word[i+1:]
                dic[mod].append(word)
        
        stack = [beginWord]
        res = 1
        visited = {beginWord}
        while stack:
            newStack = []
            while stack:
                word = stack.pop()
                if word == endWord:
                    return res
                for i in range(len(word)):
                    mod = word[:i] + "*" + word[i+1:]
                    for w in dic[mod]:
                        if w not in visited:
                            newStack.append(w)
                            visited.add(w)
            stack=newStack
            res += 1
        return 0
                

        