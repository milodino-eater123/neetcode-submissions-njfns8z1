from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hmap = defaultdict(int)

        for c in s:
            s_hmap[c] += 1
        
        for c in t:
            s_hmap[c] -= 1
        
        for key,value in s_hmap.items():
            if value != 0:
                return False
        
        return True

        