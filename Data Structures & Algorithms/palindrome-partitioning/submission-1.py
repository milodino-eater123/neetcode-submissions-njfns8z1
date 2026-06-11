class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def palin(string):
            l,r=0,len(string)-1
            while r>l:
                if string[r]!=string[l]:
                    return False
                r-=1
                l+=1
            return True
        res = []
        def build(i,path,string):
            if i>=len(s):
                if not string:
                    res.append(path.copy())
                return
            string+=s[i]
            if string and palin(string):
                path.append(string)
                build(i+1,path,"")
                path.pop()
            build(i+1,path,string)  
        build(0,[],"")
        return res


        