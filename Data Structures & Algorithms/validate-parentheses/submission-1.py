class Solution:
    def isValid(self, s: str) -> bool:
        dic = {
            '(' : ')',
            '[': ']',
            '{': '}'
        }
        stack = []
        for c in s:
            if c in dic.keys():
                stack.append(c)
            elif c in dic.values():
                if not stack:
                    return False
                elif dic[stack.pop()] != c:
                    return False
        
        if stack:
            return False
        else:
            return True