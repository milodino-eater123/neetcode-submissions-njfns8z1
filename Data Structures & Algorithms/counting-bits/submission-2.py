class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]
        
        for i in range(1,n+1):
            prevN = i-1
            prevBits = res[-1]
            while prevN&1:
                prevN>>=1
                prevBits-=1
            res.append(prevBits+1)
        return res

        