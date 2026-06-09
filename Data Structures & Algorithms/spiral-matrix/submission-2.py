class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n,m=len(matrix),len(matrix[0])
        res,count,x,y,dirs,steps = [],0,0,-1,[(0,1),(1,0),(0,-1),(-1,0)],1
        while steps:
            dir=dirs[count%4]
            side = count%2
            steps = n-1-(count//2) if side else m-(count//2)
            for i in range(steps):
                x+=dir[0]
                y+=dir[1]
                res.append(matrix[x][y])
            count+=1
        return res