class Solution:
    def isPalindrome(self, s: str) -> bool:

        #clean this stupid string
        s = "".join(c for c in s if c.isalnum())
        s = s.upper()
        
        l,r = 0,len(s)-1
        while r>l:
            if s[r] != s[l]:
                return False
            r -= 1
            l += 1 
        
        return True




        