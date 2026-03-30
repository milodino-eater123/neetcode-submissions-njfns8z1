from collections import defaultdict
class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        noEndPair, EndPair = 1, 0 
        for i in range(1,len(s)): 
            if s[i] == "0" and noEndPair == 0:
                return 0
            temp = noEndPair
            noEndPair = EndPair + noEndPair if s[i] != "0" else 0
            EndPair = temp if int(s[i-1]+s[i]) <= 26 else 0
        
        return noEndPair + EndPair