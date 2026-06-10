# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def build(i, lst):
            if not lst:
                return None
            node = TreeNode(preorder[i])
            j = lst.index(preorder[i])
            node.left = build(i + 1, lst[:j])
            node.right = build(i + 1 + j, lst[j+1:])
            return node

        return build(0, inorder)