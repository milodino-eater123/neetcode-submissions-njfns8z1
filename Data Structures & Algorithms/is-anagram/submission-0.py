from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #parse string1 into hmap
        hmap = defaultdict(int)
        for c in s:
            hmap[c] += 1
        #check string2 against hmap
        for c in t:
            if c not in hmap:
                return False
            hmap[c] -= 1
            if hmap[c] == 0:
                del hmap[c]
        if hmap:
            return False
        return True
