from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #0.5 hmap letters needed
        hmap = defaultdict(int)
        unique_letters_needed = 0
        for c in t:
            hmap[c] -= 1 
            if hmap[c] == -1:
                unique_letters_needed += 1 

        #extra - initialise varialbes
        l,r = -1,-1
        res = (0,float('inf'))

        #1. expand window until valid
        def expand_window():
            nonlocal l,r,unique_letters_needed
            while unique_letters_needed != 0:
                r += 1 
                if r == len(s):
                    return True
                if s[r] in hmap:
                    hmap[s[r]] += 1
                    if hmap[s[r]] == 0:
                        unique_letters_needed -= 1 
        #2. shrink window until not valid
        def shrink_window():
            nonlocal l,r,res,unique_letters_needed
            while unique_letters_needed == 0:
                if l == len(s):
                    return True
                l += 1 
                if s[l] in hmap:
                    hmap[s[l]] -= 1 
                    if hmap[s[l]] == -1:
                        unique_letters_needed += 1 
            if r - l < res[1] - res[0]:
                    res = (l,r)
            
        
        while True:
            if expand_window():
                break
            if shrink_window():
                break

        if res == (0,float('inf')):
            return ""
        else:
            return s[res[0]:res[1]+1]
               

        

        