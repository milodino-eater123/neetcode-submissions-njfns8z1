# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        temp = []
        cur_level = 1 
        queue = deque([(root,1)])
        while queue:
            node,level = queue.popleft()
            if level > cur_level:
                res.append(temp)
                temp = []
                cur_level += 1 
            if node:
                temp.append(node.val)
                queue.append((node.left,level+1))
                queue.append((node.right,level+1))
 
        return res


                
             
        
        