class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def build(openTotal,openAvail,path):
            if openTotal == n and openAvail == 0:
                res.append(path)
                return

            if openTotal < n:
                build(openTotal+1,openAvail+1,path+"(")
            
            if openAvail > 0:
                build(openTotal,openAvail-1,path+")")
                
        
        build(0,0,"")
        return res
