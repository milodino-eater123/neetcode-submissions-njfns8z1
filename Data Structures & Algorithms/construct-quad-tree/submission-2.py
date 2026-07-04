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
                return node
            
            mid_i,mid_j = (i1+i2)//2,(j1+j2)//2
            tLeft = quad(i1,j1,mid_i,mid_j)
            tRight = quad(i1,mid_j+1,mid_i,j2)
            bLeft = quad(mid_i+1,j1,i2,mid_j)
            bRight = quad(mid_i+1,mid_j+1,i2,j2)

            if tLeft.val==tRight.val==bLeft.val==bRight.val and tLeft.val!=1000:
                return Node(tLeft.val,True,None,None,None,None)
            else:
                return Node(1000,False,tLeft,tRight,bLeft,bRight)
                
        return quad(0,0,n-1,n-1)
        