class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n,m = len(board),len(board[0])
        def dfs(i,j):
            if i<0 or j<0 or i>=n or j>=m:
                return
            if board[i][j] == "X" or board[i][j] == "2":
                return

            board[i][j] = "2"

            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)

       
        for j in range(m):
            dfs(0,j)
            dfs(n-1,j)

        
        for i in range(n):
            dfs(i,0)
            dfs(i,m-1)

        for i in range(n):
            for j in range(m):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "2":
                    board[i][j] = "O"



        