# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = ""
        def read(node):
            nonlocal res
            res += str(node.val) + "#" if node else 'n'
            if node:
                read(node.left)
                read(node.right)
        read(root)
        print(res)
        return res

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        lst = []
        num = ''
        for c in data:
            if c == 'n':
                lst.append(None)
            elif c == '#':
                lst.append(int(num))
                num = ''
            else:
                num += c 
        print(lst)
        
        i=0
        def build():
            nonlocal i
            if not lst[i]:
                i += 1
                return None
            else:
                node = TreeNode(lst[i])
                i += 1
                node.left = build()
                node.right = build()
                return node
        return build()
            

