class Solution:
    def countSubstrings(self, s: str) -> int:
        t = '#' + '#'.join(s) + '#'
        n = len(t)
        p = [0]*n
        l,r = -1,-1
        for i in range(n):
            if l<=i<=r:
                mid = (l+r)//2
                os = i - mid
                mirr = mid - os 
                p[i] = min(p[mirr],r-i)
            while i+p[i]+1<n and i-p[i]-1>=0 and t[i+p[i]+1]==t[i-p[i]-1]:
                p[i]+=1
        
        return sum((val+1)//2 for val in p)
        