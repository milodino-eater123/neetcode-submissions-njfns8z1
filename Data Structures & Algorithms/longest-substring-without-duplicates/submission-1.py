class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1 :
            return len(s)

        #initialise variables
        res = 0
        l,r = 0,1
        hset = {s[0]}
        #iterate through s
        while r < len(s):
            if s[r] in hset:
                while s[l] != s[r]:
                    hset.remove(s[l])
                    l += 1 
                hset.remove(s[l])
                l += 1 

            hset.add(s[r])
            res = max(res,r-l+1)
            r += 1 
        return res


        