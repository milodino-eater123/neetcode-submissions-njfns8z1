from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        hmap = defaultdict(int)
        maxf = 0

        for i in range(len(s)):
            hmap[s[i]] += 1
            maxf = max(maxf,hmap[s[i]])
            
            while i - l + 1 - maxf > k:
                hmap[s[l]] -= 1
                l += 1
        
        return i - l + 1


        