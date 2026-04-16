# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        def travel(node):
            nonlocal res
            if not node:
                return
            
            res.append(node.val)
            
            travel(node.left)

            travel(node.right)
        
        travel(root)
        return res
        