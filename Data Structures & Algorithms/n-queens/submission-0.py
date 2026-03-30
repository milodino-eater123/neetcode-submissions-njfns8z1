class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        rows = [0] * n 
        cols = [0] * n 
        diag1 = [0] * (n*2-1)
        diag2 = [0] * (n*2-1)


        def build(i,j,string,path,queens):
            nonlocal res,rows,cols,diag1,diag2
            if queens == n and i == n:
                res.append(path.copy())
                return
            if i == n:
                return 

            #choice 1: put queen
            if rows[i] == 0 and cols[j] == 0 and diag1[i-j] == 0 and diag2[i+j] == 0:
                rows[i] = 1 
                cols[j] = 1 
                diag1[i-j] = 1
                diag2[i+j] = 1 
                if j == n-1:
                    path.append(string +"Q")
                    build(i+1,0,"",path,queens+1)
                    path.pop()
                    
                else:
                    build(i,j+1,string+"Q",path,queens+1)
                rows[i] = 0
                cols[j] = 0
                diag1[i-j] = 0
                diag2[i+j] = 0

           
            #choice 2: put nothing
            if j == n - 1 :
                path.append(string+".")
                build(i+1,0,"",path,queens)
                path.pop()
            else:
                build(i,j+1,string+".",path,queens)

        build(0,0,"",[],0)
        return res
        

        
        