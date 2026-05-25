class Solution:
    def myPow(self, x: float, n: int) -> float:
        m = 1
        initial=x
        while m<n:
            x*=x
            m*=2
        
        r=m-n
        for i in range(r):
            x/=initial
        return x