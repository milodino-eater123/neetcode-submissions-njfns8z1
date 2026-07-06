class Solution:
    def longestPalindrome(self, s: str) -> str:
        t = '#' + '#'.join(s) + '#'
        n = len(t)
        p = [0]*n
        l,r = -1,-1
        for i in range(n):
            if l<=i<=r:
                mid = (l+r)//2
                os = i - mid
                mirr = mid - os 
                p[i] = min(mirr-l,r-i)
            while i+p[i]+1<n and i-p[i]-1>=0 and t[i+p[i]+1]==t[i-p[i]-1]:
                p[i]+=1
        
        resLen, center_idx = max((v, i) for i, v in enumerate(p))
        resIdx = (center_idx - resLen) // 2
        return s[resIdx : resIdx + resLen]
        
                        
        