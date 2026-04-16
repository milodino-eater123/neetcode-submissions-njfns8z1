# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        def travel(node):
            nonlocal res
            if not node:
                return
            
            travel(node.left)

            res.append(node.val)

            travel(node.right)
        
        travel(root)
        return res
        