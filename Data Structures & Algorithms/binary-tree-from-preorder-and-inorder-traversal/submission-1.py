# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def build(i,inorder):
            if i>=len(preorder):
                return None
            if preorder[i] not in inorder:
                return None
            node = TreeNode(preorder[i])
            j = inorder.index(preorder[i])

            node.left=build(i+1,inorder[:j])
            node.right=build(i+j+1,inorder[j+1:])
            return node

        
        return build(0,inorder)