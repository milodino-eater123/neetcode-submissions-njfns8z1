class Solution:
    def isPalindrome(self, s: str) -> bool:
        #left and right pointers iterate down list from opp ends
        # -check if left = right
        #stop condition: left > right. Bc still have to check when 
        #left = right

        #clean this stupid string
        s = "".join(c for c in s if c.isalnum())
        s = s.upper()
        l,r = 0, len(s) - 1 
        #if any of the left-right pairs are unequal, return false
        while r >= l:
            if s[r] != s[l]:
                return False
            l += 1
            r -= 1 

        return True




        