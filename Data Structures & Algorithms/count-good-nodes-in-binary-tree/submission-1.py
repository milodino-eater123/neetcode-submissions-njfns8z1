# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def good(node,maxVal):
            if not node:
                return 0
            
            os = int(node.val>=maxVal)
            newMax = max(maxVal,node.val)
            return os + good(node.left,newMax) + good(node.right,newMax)

        return good(root,root.val)
        
        