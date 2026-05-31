class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n,m = len(board),len(board[0])
        def dfs(i,j):
            if i<0 or j<0 or i==n or j==m or board[i][j] != "O":
                return 
            board[i][j]=0

            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
            
        for i in range(n):
            for j in range(m):
                if i==0 or j==0 or i==n-1 or j==m-1:
                    dfs(i,j)       
        for i in range(n):
            for j in range(m):
                if board[i][j]==0:
                    board[i][j]="O"
                else:
                    board[i][j]="X"
            
           


       


        