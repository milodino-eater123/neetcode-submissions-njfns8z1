class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        col,diag1,diag2 = [False]*n,set(),set()
        def queen(i,q,board):
            if q==n:
                res.append(board.copy())
            for j in range(n):
                if col[j] or (i+j) in diag1 or (i-j) in diag2:
                    continue
                row = "."*j+"Q"+"."*(n-j-1)
                board.append(row)
                col[j]=True
                diag1.add(i+j)
                diag2.add(i-j)
                queen(i+1,q+1,board)
                board.pop()
                col[j]=False
                diag1.remove(i+j)
                diag2.remove(i-j)


        queen(0,0,[])
        return res
        