
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        hmap = {}
        for i,ltr in enumerate(s):
            if ltr in hmap:
                hmap[ltr][1] = i
            else:
                hmap[ltr] = [i,i]
        
        #initialise
        l,r = 0,0
        while r < len(s):
            maxRange = hmap[s[l]][1]
            while r <= maxRange:
                maxRange = max(maxRange,hmap[s[r]][1])
                r += 1 

            res.append(r-l)
            l = r 
        
        return res


            

        
        



        