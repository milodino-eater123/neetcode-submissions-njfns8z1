# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')
        def suhm(node):
            nonlocal res
            if not node:
                return 0
            
            threeSum = node.val+suhm(node.right)+suhm(node.left)
            better = max(node.val+suhm(node.right),node.val+suhm(node.left))
            best = max(better,threeSum,node.val)
            res = max(res,best)
            
            return max(better,node.val)
        
        suhm(root)
        return res
        