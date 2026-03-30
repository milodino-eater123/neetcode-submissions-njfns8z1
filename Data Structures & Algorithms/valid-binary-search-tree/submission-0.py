# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res = True
        def validate(node,left,right):
            nonlocal res
            if not node:
                return True

            if not left < node.val < right:
                res = False
                return 

            validate(node.left,left,node.val) 
            validate(node.right,node.val,right) 

        validate(root,float("-inf"),float("inf"))
        return res 

        