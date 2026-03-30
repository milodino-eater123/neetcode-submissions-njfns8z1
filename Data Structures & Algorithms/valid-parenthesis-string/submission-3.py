class Solution:
    def checkValidString(self, s: str) -> bool:
        minOpen = 0
        maxOpen = 0
        for c in s:
            if c == "(":
                minOpen += 1
                maxOpen += 1 
            elif c == ")" :
                minOpen -= 1 
                maxOpen -= 1 
            elif c == "*":
                minOpen -= 1 
                maxOpen += 1 

            if maxOpen < 0:
                return False
            if minOpen < 0:
                minOpen = 0

            #maxOpen checks for if too many )
            #max ( still too many ), means for all n ) is too many

            #minOpen checks if too many ((
            #min ( still too many (, means for all n ( it is too many
        
        return True if minOpen == 0 else False
        