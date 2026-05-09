# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def check(n1,n2):
            if not n1 and not n2:
                return True

            
            return bool(n1 and n2) and (n1.val==n2.val) and check(n1.left,n2.left) and check(n1.right,n2.right)

        return check(p,q)
        

        