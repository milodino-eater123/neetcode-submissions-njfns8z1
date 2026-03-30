from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #iterate through strs

        #store in set/dict -> each string must be list/tuple, not dict
        #you can store the anagram value of each string as a list because of finite alphabets
        #store the words in the dictionary values as a list
        hmap = defaultdict(list)
        for string in strs:
            anagram_val = [0] * 26
            for c in string:
                i = ord(c) - ord('a')
                anagram_val[i] += 1 
            hmap[tuple(anagram_val)].append(string) 
        return list(hmap.values())   
        
            