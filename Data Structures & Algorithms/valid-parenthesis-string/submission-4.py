class Solution:
    def checkValidString(self, s: str) -> bool:
        openBracket = []
        star = []

        for i,c in enumerate(s):
            if c == "(":
                openBracket.append(i)
            elif c == "*":
                star.append(i)
            elif c == ")":
                if openBracket:
                    openBracket.pop()
                elif star:
                    star.pop()
                else:
                    return False
            
        while openBracket:
            if not star:
                return False
            if openBracket.pop() > star.pop():
                return False
            
        return True
            


        