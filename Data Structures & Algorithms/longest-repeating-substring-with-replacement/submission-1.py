from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #sw, highest freq count + k  = total length of sw

        #track hmap,highest freq count, total length
        
        l,r = 0,0
        hmap = defaultdict(int)
        highest_freq = 0
        res = 0

        while r < len(s):
            #if "not enough k"
            hmap[s[r]] += 1 
            highest_freq = max(highest_freq,hmap[s[r]])

            while highest_freq + k < (r-l+1):
                hmap[s[l]] -= 1 
                l += 1 
            
 
            res = max(res,r-l+1)
            r += 1      
        
        return res

        