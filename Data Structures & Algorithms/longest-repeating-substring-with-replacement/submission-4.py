from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,maxFreq=0,0
        hmap = defaultdict(int)
        for i in range(len(s)):
            hmap[s[i]]+=1
            maxFreq=max(maxFreq,hmap[s[i]])
            while (i-l+1) > maxFreq+k:
                hmap[s[l]]-=1
                l+=1
            
        
        return len(s)-l
            
            
        