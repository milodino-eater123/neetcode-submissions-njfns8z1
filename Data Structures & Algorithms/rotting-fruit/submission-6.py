class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = 0
        n,m = len(grid),len(grid[0])
        stack = []
        visited = set()
        fresh = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==2:
                    stack.append((i,j))
                if grid[i][j]==1:
                    fresh += 1
        
        while fresh>0 and stack:
            newStack = set()
            rotted = False
            while stack:
                i,j = stack.pop()
                if i<0 or j<0 or i>=n or j>=m:
                    continue
                if grid[i][j] == 0:
                    continue
                if (i,j) in visited:
                    continue
                
                if grid[i][j]==1:
                    fresh -= 1
                    rotted = True
                visited.add((i,j))
                
                newStack.add((i+1,j))
                newStack.add((i-1,j))
                newStack.add((i,j+1))
                newStack.add((i,j-1)) 
            if rotted:           
                time += 1
                rotted = not rotted
            stack = list(newStack)
        
        return time if not fresh else -1
                


        
