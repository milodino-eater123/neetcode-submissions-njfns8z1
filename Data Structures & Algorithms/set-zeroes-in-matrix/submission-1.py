class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n,m = len(matrix),len(matrix[0])
        def setz(i,j):
            if matrix[i][j]!=0:
                return
            
            for x in range(n):
                if matrix[x][j] == 0:
                    continue
                matrix[x][j] = "0"
            
            for y in range(m):
                if matrix[i][y]==0:
                    continue
                matrix[i][y]="0"
            
        for i in range(n):
            for j in range(m):
                setz(i,j)
        
        for i in range(n):
            for j in range(m):
                matrix[i][j]==int(matrix[i][j])
        
        