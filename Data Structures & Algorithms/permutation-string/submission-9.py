from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hmap = defaultdict(int)

        #edge case:
        if len(s1) > len(s2):
            return False
        
        #map char frequencies of s1
        for c in s1:
            hmap[c] -= 1

        
        #intialise window
        for i in range(len(s1)):
            hmap[s2[i]] += 1
            if hmap[s2[i]] == 0:
                del hmap[s2[i]]
        
        #slide window
        l,r = 0,len(s1)
        while r < len(s2):
            if not hmap:
                return True
            
            hmap[s2[l]] -= 1
            hmap[s2[r]] += 1
            if hmap[s2[l]] == 0:
                del hmap[s2[l]]
            if hmap[s2[r]]== 0:
                del hmap[s2[r]]
            l += 1
            r += 1
        
        return not hmap

       

        



        