# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return False
        def check(node1,node2):
            if not node1 and not node2:
                return True
            elif not node1 or not node2:
                return False
            
            if node1.val != node2.val:
                return False
            
            return check(node1.left,node2.left) and check(node1.right,node2.right)
        
        res = False
        def checker(node):
            nonlocal res
            if not node:
                return
            
            if node.val == subRoot.val:
                if check(node,subRoot):
                    res = True
                    return

            checker(node.left)
            checker(node.right)
        
        checker(root)
        return res

            


        
        