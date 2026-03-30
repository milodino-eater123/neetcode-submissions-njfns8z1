class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n,m = len(grid),len(grid[0])
        def bfs(i,j):
            stack = [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]
            dist = 1
            visited = set()
            while stack:
                newStack = set()
                while stack:
                    i,j = stack.pop()
                    if (i,j) in visited or i<0 or j<0 or i>=n or j>=m or grid[i][j]==-1 or grid[i][j]==0:
                        continue
                    grid[i][j] = min(grid[i][j],dist)
                    visited.add((i,j))
                    newStack.add((i+1,j))
                    newStack.add((i-1,j))
                    newStack.add((i,j+1))
                    newStack.add((i,j-1))
                dist += 1
                stack = list(newStack)
            
        for i in range(n):
                for j in range(m):
                    if grid[i][j] == 0:
                        bfs(i,j)

        