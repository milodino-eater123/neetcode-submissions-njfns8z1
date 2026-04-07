# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        #1,2,None,None,3,4,None,None,5,None,None
        res = ""
        q = deque([root])
        while q:
            node = q.popleft()
            val = node.val if node else "N"
            res += str(val)
            res += "."
            if node:
                q.append(node.left)
                q.append(node.right)
        return res
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "N.":
            return
         
        data = data.split(".")
        data.pop()
        data = [int(x) if x != "N" else x for x in data]
        root = TreeNode(data[0])
        stack = [root]
        i = 1
        #1,2,3,N,N,4,5,N,N,N,N
        while stack:
            newStack = []
            for node in stack:
                if not node:
                    continue
                if i<len(data) and data[i] != "N":
                    node.left = TreeNode(data[i])
                    newStack.append(node.left)
                if i+1<len(data) and data[i+1] != "N":
                    node.right = TreeNode(data[i+1])
                    newStack.append(node.right)
                i+=2
            stack = newStack
        return root

