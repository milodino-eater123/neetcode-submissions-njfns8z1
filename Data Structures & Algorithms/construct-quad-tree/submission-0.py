"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)
        def quad(i1,j1,i2,j2):
            if i1==i2:
                node = Node(grid[i1][j1],True,None,None,None,None)
                return node,grid[i1][j1]
            
            mid_i,mid_j = (i1+i2)//2,(j1+j2)//2
            topLeft,val1 = quad(i1,j1,mid_i,mid_j)
            topRight,val2 = quad(i1,mid_j+1,mid_i,j2)
            bottomLeft,val3 = quad(mid_i+1,j1,i2,mid_j)
            bottomRight,val4 = quad(mid_i+1,mid_j+1,i2,j2)

            if val1==val2==val3==val4 and val1!=1000:
                return Node(val1,True,None,None,None,None),val1
            else:
                return Node(1000,False,topLeft,topRight,bottomLeft,bottomRight),1000
                
        return quad(0,0,n-1,n-1)[0]
        