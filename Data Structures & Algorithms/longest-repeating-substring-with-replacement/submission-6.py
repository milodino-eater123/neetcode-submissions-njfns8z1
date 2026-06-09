from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,hmap,maxFreq=0,defaultdict(int),0
        for i,c in enumerate(s):
            hmap[c]+=1
            maxFreq=max(maxFreq,hmap[c])
            if maxFreq+k<i-l+1:
                hmap[s[l]]-=1
                l+=1
        return len(s)-l

        