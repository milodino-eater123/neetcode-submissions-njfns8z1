class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n,m = len(heights),len(heights[0])
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        def bfs(stack,sea):
            while stack:
                newStack = set()
                while stack:
                    x,y = stack.pop()
                    sea.add((x,y))
                    for dx,dy in dirs:
                        i,j = x+dx,y+dy
                        if i<0 or j<0 or i==n or j==m or (i,j) in sea:
                            continue
                        if heights[i][j]<heights[x][y]:
                            continue
                        newStack.add((i,j))
                stack=list(newStack)
        
        inPacific,inAtlantic = set(),set()
        stack1 = [(0,j) for j in range(m)] + [(i,0) for i in range(1,n)]
        stack2 = [(n-1,j) for j in range(m)] + [(i,m-1) for i in range(n-1)]

        bfs(stack1,inPacific)
        bfs(stack2,inAtlantic)

        return list(inPacific&inAtlantic)


                    

                
            