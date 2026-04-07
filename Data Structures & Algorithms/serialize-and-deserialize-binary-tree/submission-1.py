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
        print(res)
        return res
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "N.":
            return
        data = list(data)
        def extractNode(i):
            val = ""
            while data[i] != ".":
                val += data[i]
                i += 1
            i += 1
            return val,i
        val,i = extractNode(0) 
        root = TreeNode(int(val))
        stack = [root]

        #1,2,3,N,N,4,5,N,N,N,N
        while stack:
            newStack = []
            for node in stack:
                if i>=len(data):
                    return root
                val,i = extractNode(i)
                if val != "N":
                    node.left = TreeNode(val)
                    newStack.append(node.left)

                if i>=len(data):
                    return root
                val,i = extractNode(i)
                if val != "N":
                    node.right = TreeNode(val)
                    newStack.append(node.right)

            stack = newStack
        return root

