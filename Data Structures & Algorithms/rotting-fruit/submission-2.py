class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n,m = len(grid),len(grid[0])
        stack = []
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    stack.append((i+1,j))
                    stack.append((i-1,j))
                    stack.append((i,j+1))
                    stack.append((i,j-1))

        minutes = 0
        while stack:
            newStack = set()
            hset = set()
            while stack:
                i,j = stack.pop()
                if i<0 or j<0 or i>=n or j>=m:
                    continue
                cell = grid[i][j]
                if cell==0 or cell==2 or (i,j) in hset:
                    continue
                grid[i][j] = 2 
                hset.add((i,j))
                newStack.add((i+1,j))
                newStack.add((i-1,j))
                newStack.add((i,j+1))
                newStack.add((i,j-1))
            if newStack:
                minutes += 1 
            stack = list(newStack)
        isPossible = True
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    isPossible = False
        
        print(grid)
        return minutes if isPossible else -1
