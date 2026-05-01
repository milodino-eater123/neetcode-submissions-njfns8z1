class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        res = 1
        l,r = 0,1
        hset = {s[l]}

        while r < len(s):
            if s[r] in hset:
                while s[l] != s[r]:
                    hset.remove(s[l])
                    l += 1
                l += 1

            else:
                res = max(res,r-l+1)
                hset.add(s[r])

            r += 1
        
        
        return res

        