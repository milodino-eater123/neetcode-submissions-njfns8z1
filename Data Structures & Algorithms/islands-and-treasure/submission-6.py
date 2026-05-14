from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n,m = len(grid),len(grid[0])
        stack = deque()
        visited = set()
        for i in range(n):
            for j in range(m):
                if grid[i][j]==0:
                    stack.append((i,j,0))
        
        while stack:
            i,j,dist = stack.popleft()
            if i<0 or j<0 or i>=n or j>=m:
                continue
            if grid[i][j] == -1:
                continue
            if (i,j) in visited:
                continue

            grid[i][j] = dist
            visited.add((i,j))
            stack.extend([
    (i-1, j, dist+1),
    (i+1, j, dist+1),
    (i, j-1, dist+1),
    (i, j+1, dist+1)
])


        

        
        

        