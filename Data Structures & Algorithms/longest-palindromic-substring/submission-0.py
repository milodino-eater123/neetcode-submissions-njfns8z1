class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxPalin = (0,0)
        for i in range(len(s)):
            l = r = i
            while l>=0 and r<len(s) and s[l] == s[r]:
                if r-l > maxPalin[1] - maxPalin[0]:
                    maxPalin = (l,r)
                l -= 1
                r += 1
        for i in range(len(s)-1):
            l,r = i,i+1
            while l>= 0 and r<len(s) and s[l] == s[r]:
                if r-l > maxPalin[1] - maxPalin[0]:
                    maxPalin = (l,r)
                l -= 1
                r += 1
        return s[maxPalin[0]:maxPalin[1]+1]
        

        