class Solution:
    def numDecodings(self, s: str) -> int:
        prev1,prev2 = 1,None
        for i,c in enumerate(s):
            if c == "0":
                if i-1>=0 and s[i-1]=="1" or s[i-1]=="2":
                    prev1,prev2=prev2,prev1   
                else:
                    return 0      
            elif i-1>=0 and 11<=int(s[i-1:i+1])<=26:
                prev1+=prev2
                prev2=prev1-prev2
            else:
                prev2=prev1
        return prev1

        