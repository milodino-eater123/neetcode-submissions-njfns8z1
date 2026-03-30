from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #edge case
        if len(s1) > len(s2):
            return False 
        #store needed letters
        hmap = defaultdict(int)
        unique_nums_needed = 0
        for c in s1:
            if c not in hmap:
                unique_nums_needed += 1 
            hmap[c] -= 1 

        #iterate through s2 with set window
        l,r = 0,-1
        while True:
            #construct window of appropriate size with hmap data
            while r < len(s1) - 1:
                r += 1 
                if s2[r] in hmap:
                    hmap[s2[r]] += 1 
                    if hmap[s2[r]] == 0:
                        unique_nums_needed -= 1 
            
            if unique_nums_needed == 0:
                return True

            if r + 1 >= len(s2):
                break
            #move window and adjust hmap data accordingly
        
            #remove s2[l] from hmap -> l += 1
            if s2[l] in hmap:
                hmap[s2[l]] -= 1 
                if hmap[s2[l]] == -1:
                    unique_nums_needed += 1 
            l += 1 

            #add s2[r+1] to hmap -> s += 1 
            if s2[r+1] in hmap:
                hmap[s2[r+1]] += 1 
                if hmap[s2[r+1]] == 0:
                    unique_nums_needed -= 1 
            r += 1 

            if unique_nums_needed == 0:
                return True
        
        return False



        