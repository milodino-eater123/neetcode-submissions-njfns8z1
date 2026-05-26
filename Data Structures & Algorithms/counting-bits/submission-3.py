class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]
        
        for i in range(n):
            prevBits = res[-1]
            while i&1:
                i>>=1
                prevBits-=1
            res.append(prevBits+1)
        return res

        