class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        visited = set()

        def translocate(i,j,val):
            if (i,j) in visited:
                return
            x,y = j,n-1-i
            temp = matrix[x][y]
            matrix[x][y] = val
            visited.add((i,j))
            translocate(x,y,temp)
        
        x=0
        y=n-1

        for _ in range(n//2):
            for j in range(y):
                translocate(x,j,matrix[x][j])
            x += 1
            y -= 1 
        