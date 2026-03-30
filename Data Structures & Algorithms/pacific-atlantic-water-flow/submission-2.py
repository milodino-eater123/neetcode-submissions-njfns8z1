class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n,m = len(heights), len(heights[0])

        inPacific = set()
        inAtlantic = set()
        stack = []
        res = set()
        for j in range(m):
            stack.append((0,j))
        
        for i in range(1,n):
            stack.append((i,0))

        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        while stack:
            newStack = set()
            while stack:
                i,j = stack.pop()
                inPacific.add((i,j))
                for one,two in directions:
                    x = i+one
                    y = j+two
                    if x<0 or y<0 or x>=n or y>=m:
                        continue
                    if heights[x][y] < heights[i][j]:
                        continue
                    if (x,y) in inPacific:
                        continue
                    newStack.add((x,y))
            stack = list(newStack)
        
        for j in range(m):
            stack.append((n-1,j))
        
        for i in range(0,n-1):
            stack.append((i,m-1))

        while stack:
            newStack = set()
            while stack:
                i,j = stack.pop()
                inAtlantic.add((i,j))
                if (i,j) in inPacific:
                    res.add((i,j))
                for one,two in directions:
                    x = i+one
                    y = j+two
                    if x<0 or y<0 or x>=n or y>=m:
                        continue
                    if heights[x][y] < heights[i][j]:
                        continue
                    if (x,y) in inAtlantic:
                        continue
                    newStack.add((x,y))
            stack = list(newStack)
        
        return [list(x) for x in res]


        #mistakes
        #1. forgot visited cases
        #2. forgot about duplicates