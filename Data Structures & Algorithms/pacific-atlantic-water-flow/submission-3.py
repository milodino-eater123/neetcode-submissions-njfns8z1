class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        res = []
        n,m = len(heights),len(heights[0])
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        def bfs(i,j,sea):
            nonlocal pacific,atlantic,res
            stack = [(i,j)]

            while stack:
                i,j = stack.pop()
                if (i,j) in atlantic and (i,j) in pacific:
                    res.append([i,j])
                for dx,dy in directions:
                    x,y = i+dx,j+dy
                    if x<0 or y<0 or x>=n or y>=m:
                        continue
                    if (x,y) in sea:
                        continue
                    if heights[x][y] < heights[i][j]:
                        continue
                    sea.add((x,y))
                    stack.append((x,y))
        
        for j in range(m):
            pacific.add((0,j))
            bfs(0,j,pacific)
        
        for i in range(1,n):
            pacific.add((i,0))
            bfs(i,0,pacific)
        
        for j in range(m):
            atlantic.add((n-1,j))
            bfs(n-1,j,atlantic)
        
        for i in range(0,n-1):
            atlantic.add((i,m-1))
            bfs(i,m-1,atlantic)
        
        return [list(x) for x in (pacific & atlantic)]
                
                
                
            