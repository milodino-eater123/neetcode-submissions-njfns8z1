class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        board = [[0]* n for _ in range(m)] 
        board[0][0] = 1
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                top = board[i-1][j] if i - 1 >= 0 else 0
                left = board[i][j-1] if j-1 >= 0 else 0
                board[i][j]= top + left
        
        return board[m-1][n-1]

        