from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = defaultdict(list)
        for string in strs:
            lst = [0] * 26
            for c in string:
                n = ord(c)-ord("a")
                lst[n]+=1
            hmap[tuple(lst)].append(string)
        
        return list(hmap.values())


        