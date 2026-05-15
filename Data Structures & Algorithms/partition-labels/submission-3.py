class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        hmap = {}
        for i,n in enumerate(s):
            hmap[n] = i
        
        l,r= 0,0

        for i in range(len(s)):
            r = max(r,hmap[s[i]])
            if i == r:
                res.append(r-l+1)
                l = i+1
        
        return res


            
            
        