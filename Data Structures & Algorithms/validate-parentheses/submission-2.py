class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hmap = {
            ")":"(",
            "]":"[",
            "}":"{",

        }
        for b in s:
            if b == "(" or b == "[" or b == "{":
                stack.append(b)
            else:
                if stack and hmap[b] == stack[-1]:
                    stack.pop()
                else:
                    return False
        
        return not bool(stack)
        