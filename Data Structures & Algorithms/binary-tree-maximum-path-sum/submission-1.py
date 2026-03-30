# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')
        def search(node):
            nonlocal res
            if not node:
                return 0
            left,right = search(node.left),search(node.right)
            
            bigger = max(left,right)
            res = max(res,node.val,node.val+bigger,node.val+left+right)
            return max(node.val,node.val+bigger)
        
        search(root)
        return res
        