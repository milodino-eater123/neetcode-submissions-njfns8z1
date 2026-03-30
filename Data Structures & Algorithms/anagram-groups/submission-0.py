from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #make a list of strings' anagram hmaps
        hmap_list = []
        for string in strs:
            hmap = defaultdict(int)
            for c in string:
                hmap[c] += 1 
            hmap_list.append(hmap)

        #initialise variables
        res = []
        counter = 0
        l = 0
        hset = set()

    
        while counter < len(strs):
            #check if left pointer in result
            if l in hset:
                l += 1
                continue
            hset.add(l)
            r = l + 1 
            temp = [strs[l]]
            while r < len(hmap_list):
                if hmap_list[r] == hmap_list[l]:
                    temp.append(strs[r])
                    hset.add(r)
                r += 1 
            res.append(temp)
            counter += len(temp)
            l += 1 
        return res
 
        
            