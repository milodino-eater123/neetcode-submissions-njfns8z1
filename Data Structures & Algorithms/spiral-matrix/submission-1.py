class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n,m = len(matrix),len(matrix[0])
        visited = set()
        res = []
        def spiral(i,j,dir):
            nonlocal res,visited
            if len(res) == (n*m):
                return
            if i<0 or j<0 or i>=n or j>=m or (i,j) in visited:
                return False
            res.append(matrix[i][j])
            visited.add((i,j))
            x,y=dir
            if spiral(i+x,j+y,dir) == False:
                newDir = (y,x) if x == 0 else (-y,-x)
                x,y = newDir
                spiral(i+x,j+y,newDir)
        spiral(0,0,(0,1))
        return res

        #(0,1),(1,0),(0,-1),(-1,0)

            

        


        spiral(0,0,(0,1))
        