class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {
            2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z']
                    }


        res = []
        def build(i,string):
            nonlocal res,dic
            if i>=len(digits):
                if string:
                    res.append(string)
                return 

            n = digits[i]
            for ltr in dic[int(n)]:
                build(i+1,string+ltr)

        build(0,"")
        return res


        