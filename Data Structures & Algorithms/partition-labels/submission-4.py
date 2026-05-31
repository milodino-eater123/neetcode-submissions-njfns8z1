class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hmap = {}
        for i,c in enumerate(s):
            hmap[c] = i
        
        res = []
        start,end = 0,0
        for i,c in enumerate(s):
            end = max(end,hmap[c])
            if i == end:
                res.append(end-start+1)
                start = i+1
        
        return res



        
        
            
            
        