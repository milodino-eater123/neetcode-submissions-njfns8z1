class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(string):
            if not string:
                return False
            l,r = 0,len(string)-1
            while r>l:
                if string[l] != string[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        res = [        ]
        def build(i,string,path):
            nonlocal res,isPalindrome
            isPalin = isPalindrome(string)
            if i >= len(s):
                if isPalin:
                    path.append(string)
                    res.append(path.copy())
                    path.pop()
                return

            c = s[i]

            build(i+1,string+c,path)

            if isPalin:
                path.append(string)
                build(i+1,c,path)
                path.pop()

        build(0,"",[])
        return res

        