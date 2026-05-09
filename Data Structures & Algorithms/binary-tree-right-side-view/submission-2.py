# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = deque([root])
        while stack:
            newStack = []
            for node in stack:
                if node:
                    res.append(node.val)
                    break
            while stack:
                node = stack.popleft()
                if not node:
                    continue
                newStack.append(node.right)
                newStack.append(node.left)
            stack = deque(newStack)
        
        return res


                    

        