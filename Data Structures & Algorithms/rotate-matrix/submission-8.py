class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        def switch(i,j):
            temp = matrix[i][j]
            matrix[i][j] = matrix[n-1-j][i]
            matrix[n-1-j][i] = matrix[n-1-i][n-1-j]
            matrix[n-1-i][n-1-j] = matrix[j][n-1-i]
            matrix[j][n-1-i]=temp
        

        half = n//2
        for i in range(half):
            for j in range(i,n-1-i):
                switch(i,j)
            