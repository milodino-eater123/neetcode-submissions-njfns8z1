from collections import defaultdict
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = defaultdict(set)
        indegrees = defaultdict(int)
        letters=set()
        for word in words:
            for c in word:
                letters.add(c)
        for i in range(0,len(words)-1):
            word1,word2 = words[i],words[i+1]
            for j in range(min(len(word1),len(word2))):
                c1,c2=word1[j],word2[j]
                if c1 != c2:
                    if c2 not in adj[c1]:
                        adj[c1].add(c2)
                        indegrees[c2] += 1
                    break
                if len(word1) > len(word2):
                    return ""
        #intialise stack with indegrees of 0
        stack = []
        for ltr in letters:
            if ltr not in indegrees:
                stack.append(ltr)
        res = ""
        while stack:
            newStack = set()
            while stack:
                ltr = stack.pop()
                res += ltr
                for c in adj[ltr]:
                    indegrees[c] -= 1 
                    if indegrees[c] == 0:
                        del indegrees[c]
                        newStack.add(c)
            stack = list(newStack)
        if indegrees:
            return ""

        return res 
        #a<b<c

                
                    




        