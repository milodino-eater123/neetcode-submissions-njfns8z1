from collections import defaultdict
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n,m = len(s1),len(s2)
        if n + m != len(s3):
            return False
        dp = defaultdict(lambda: False)
        dp[(n,m)] = True

        stack = [(n-1,m),(n,m-1)]

        while stack:
            newStack = set()
            while stack:
                i,j = stack.pop()
                if i < 0 or j < 0:
                    continue
                left = (s1[i] == s3[i+j] and dp[(i+1,j)]) if i<len(s1) else False
                right = (s2[j]==s3[i+j] and dp[(i,j+1)]) if j<len(s2) else False
                dp[(i,j)] = left or right
                newStack.add((i-1,j))
                newStack.add((i,j-1))
            stack = list(newStack)
        
        return dp[0,0]


            


