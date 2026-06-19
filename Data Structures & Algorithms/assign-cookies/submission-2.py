class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(reverse=True)
        s.sort(reverse=True)
        res = 0
        j = 0
        for child in g:
            if j<len(s) and s[j]>=child:
                res += 1
                j += 1 
        return res
        