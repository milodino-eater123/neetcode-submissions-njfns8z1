class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = strs[0]

        def combine(s1,s2):
            output = ""
            if len(s1)<len(s2):
                less, more = s1,s2
            else:
                more,less = s1,s2
            
            for i in range(len(less)):
                if s1[i] == s2[i]:
                    output += s1[i]
                else:
                    break

            return output
            

        for s in strs[1:]:
            res = combine(res,s)
        
        return res
        