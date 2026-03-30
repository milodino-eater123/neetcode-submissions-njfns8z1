class Solution:
    def countSubstrings(self, s: str) -> int:
        def isPalin(string):
            if not string:
                return False
            l,r = 0,len(string)-1
            while r >= l:
                if string[l] != string[r]:
                    return False
                l += 1
                r -= 1 
            return True
        res = 0
        def explore(i,String,prev):
            nonlocal res, isPalin
            if String and prev == ".":
                res += 1 
                return
            if i >= len(s):
                if isPalin(String):
                    res += 1
                return

            if not (String and not isPalin(String)):
                explore(i+1,String,".")

            c = s[i]
            explore(i+1,String+c,"ltr")
            

        explore(0,"",None)
        return res
        