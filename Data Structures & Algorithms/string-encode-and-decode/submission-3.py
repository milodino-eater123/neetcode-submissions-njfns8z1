class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            res += str(len(string))+"#"+string
        
        return res
        

    def decode(self, s: str) -> List[str]:
        res = []
        l,r=0,0
        while l<len(s):
            while s[r] != "#":
                r += 1
            n = int(s[l:r])      
            res.append(s[r+1:r+n+1])
            r += n+1
            l = r
        
        return res


