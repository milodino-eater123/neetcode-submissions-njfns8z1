from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dic1 = defaultdict(int)
        dic2 = defaultdict(int)
        for c in s1:
            dic1[c]+=1
        
        l=0
        for i,c in enumerate(s2):
            dic2[c]+=1
            if i-l+1>len(s1):
                c=s2[l]
                dic2[c]-=1
                if not dic2[c]:
                    del dic2[c]
                l += 1
            if dic1==dic2:
                return True
        return False

        