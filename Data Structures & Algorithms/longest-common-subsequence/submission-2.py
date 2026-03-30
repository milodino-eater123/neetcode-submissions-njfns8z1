from collections import defaultdict
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)-1
        m = len(text2) -1
        stack =[(n,m)]
        dp = defaultdict(int)
        carry_dp = defaultdict(int)
        while stack:
            newStack = set()
            new_dp = defaultdict(int)
            while stack:
                i,j = stack.pop()
                if i >= len(text1) or j >= len(text2) or i<0 or j<0:
                    continue
                if text1[i] == text2[j]:
                    new_dp[i,j] += 1 
                    new_dp[i,j] += dp[i+1,j+1]
                else:
                    new_dp[i,j] += max(dp[i+1,j],dp[i,j+1])
                newStack.add((i-1,j))
                newStack.add((i,j-1))
            dp = new_dp | carry_dp
            carry_dp = new_dp
            stack = list(newStack)
        return dp[(0,0)]



