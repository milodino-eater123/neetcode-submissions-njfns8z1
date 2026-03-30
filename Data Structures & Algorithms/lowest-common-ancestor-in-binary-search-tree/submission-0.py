# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        res = 0
        def search(node):
            nonlocal res
            if not node:
                return
            if p.val > node.val and q.val>node.val:
                search(node.right)
            elif p.val < node.val and q.val < node.val:
                search(node.left)
            else:
                res = node
                return
        search(root)
        return res

        