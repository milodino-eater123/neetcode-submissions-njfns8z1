# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        def travel(node):
            nonlocal res
            if not node:
                return
            
            travel(node.left)

            travel(node.right)

            res.append(node.val)
        
        travel(root)
        return res
        
        