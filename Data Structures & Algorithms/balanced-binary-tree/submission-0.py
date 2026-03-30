# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True
        def measure(node):
            nonlocal res
            if not node:
                return -1
            
            left = measure(node.left)
            right = measure(node.right)

            if abs(right-left) > 1:
                res = False

            return max(left,right) + 1 

        measure(root)
        return res


            
        