class Solution:
    def checkValidString(self, s: str) -> bool:
        maxOpen,minOpen = 0,0

        for c in s:
            if c == ')':
                maxOpen -= 1
                minOpen -= 1
            elif c == '(':
                maxOpen += 1
                minOpen += 1
            else:
                maxOpen += 1
                minOpen -= 1
            if maxOpen < 0:
                    return False
            if minOpen < 0:
                minOpen = 0
        return minOpen <= 0
        



        
        
        
        



        