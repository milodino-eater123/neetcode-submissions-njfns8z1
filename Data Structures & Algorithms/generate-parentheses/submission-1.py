class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def bracket(string,opens,closes):
            nonlocal res
            if opens == n and closes == n:
                res.append(string)
                

            if opens < n:
                bracket(string+"(",opens+1,closes)
            
            if closes < n and opens > closes:
                bracket(string+")",opens,closes+1)
        bracket("",0,0)
        return res
        