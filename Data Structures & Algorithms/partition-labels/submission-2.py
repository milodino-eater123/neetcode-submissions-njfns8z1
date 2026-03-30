from collections import defaultdict
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hmap = defaultdict(int)
        for i,ltr in enumerate(s):
            hmap[ltr] = max(hmap[ltr],i)
        res = []
        End = size = 0
        for i,ltr in enumerate(s):
            size += 1
            End = max(End,hmap[ltr])
            if i == End:
                res.append(size)
                size = 0
        
        return res
            
            


        