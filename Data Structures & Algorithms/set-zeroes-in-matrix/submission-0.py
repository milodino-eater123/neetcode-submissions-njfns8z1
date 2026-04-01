class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n,m = len(matrix),len(matrix[0])
        def setCell(i,j):
            #set row
            for y in range(m):
                if matrix[i][y]==0:
                    continue
                matrix[i][y] = -1
            for x in range(n):
                if matrix[x][j]==0:
                    continue
                matrix[x][j]  = -1
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    setCell(i,j)
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==-1:
                    matrix[i][j]=0
        
        