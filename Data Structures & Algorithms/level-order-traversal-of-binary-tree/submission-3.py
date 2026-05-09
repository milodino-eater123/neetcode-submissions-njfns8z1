# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        stack = deque([root])
        while stack:
            newStack = []
            level = []
            while stack:
                node = stack.popleft()
                if not node:
                    continue
                level.append(node.val)
                newStack.append(node.left)
                newStack.append(node.right)
            if level:
                res.append(level)
            stack = deque(newStack)
        
        return res
