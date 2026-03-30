from collections import defaultdict
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if not s1 and not s2 and not s3:
            return True
        n,m = len(s1),len(s2)
        if n + m != len(s3):
            return False
        dp = {}
        dp[(n,m)] = True

        stack = [(n-1,m),(n,m-1)]

        while stack:
            newStack = set()
            newDP = {}
            while stack:
                i,j = stack.pop()
                if i<0 or j<0:
                    continue
                left = (s1[i] == s3[i+j] and dp[(i+1,j)]) if i<len(s1) else False
                right = (s2[j]==s3[i+j] and dp[(i,j+1)]) if j<len(s2) else False
                newDP[(i,j)] = left or right
                if i-1 >= 0:
                    newStack.add((i-1,j))
                if j-1 >= 0:
                    newStack.add((i,j-1))
            stack = list(newStack)
            dp = newDP
        
        return dp[(0,0)]


            


