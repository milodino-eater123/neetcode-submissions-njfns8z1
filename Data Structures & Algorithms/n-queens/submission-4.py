class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        row,col,diag1,diag2 = [False]*n,[False]*n,set(),set()
        def queen(i,board,q):
            if i==(n*n):
                if q==n:
                    res.append(board.copy())
                return
            if len(board[-1])==n:
                board.append("")
            x,y = i//n,i%n
            if not row[x] and not col[y] and (x+y) not in diag1 and (x-y) not in diag2:
                row[x],col[y] = True,True
                diag1.add(x+y)
                diag2.add(x-y)
                board[-1]+="Q"
                queen(i+1,board,q+1)
                board[-1]=board[-1][:-1]
                row[x],col[y]=False,False
                diag1.remove(x+y)
                diag2.remove(x-y)
            
           
            board[-1]+="."
            queen(i+1,board,q)
            board[-1]=board[-1][:-1]
            if not board[-1]:
                board.pop()
            

        queen(0,[""],0)
        return res
        