from collections import defaultdict
class Solution:
    def numDecodings(self, s: str) -> int:
        res = 0
        hmap = defaultdict(int)
        def dfs(i,lastDigit):
            nonlocal res
            if (i,lastDigit) in hmap:
                return hmap[(i,lastDigit)]
            if i >= len(s):
                if not lastDigit:
                    return 1 
                return 0 
            n=s[i]
            if n == "0" and not lastDigit:
                return 0 
            
            string = lastDigit + n
            #choice 1, decode
            decode = dfs(i+1,"") if int(string)<=26 else 0
                
            hold = dfs(i+1,n) if not lastDigit and (n=="1"or n=="2") else 0

            hmap[(i,lastDigit)] = decode + hold
            return decode + hold
                

        return dfs(0,"")
