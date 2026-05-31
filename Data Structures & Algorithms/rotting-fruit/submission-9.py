class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n,m = len(grid),len(grid[0])
        fresh,stack = 0,[]
        for i in range(n):
            for j in range(m):
                v = grid[i][j]
                fresh += int(v==1)
                if v==2:
                    stack.append((i,j))
        if fresh==0:
            return 0
        
        dirs,minutes = [(1,0),(-1,0),(0,1),(0,-1)],0
        while stack:
            newStack = []
            while stack:
                x,y = stack.pop()
                for dx,dy in dirs:
                    i,j=x+dx,y+dy
                    if i<0 or j<0 or i==n or j==m or grid[i][j] != 1:
                        continue
                    grid[i][j]=2
                    fresh-=1
                    newStack.append((i,j))
            minutes += int(bool(newStack))
            stack = newStack
            if fresh==0:
                return minutes
        
        return -1



        
