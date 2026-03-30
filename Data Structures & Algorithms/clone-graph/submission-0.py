"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import defaultdict
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        nodes = defaultdict(lambda: Node(0))
        visited = set()
        def dfs(node):
            if node in visited:
                return
            i = node.val
            nodes[i].val = i
            nodes[i].neighbors = [nodes[x.val] for x in node.neighbors]
            visited.add(node)
            for child in node.neighbors:
                dfs(child)

        dfs(node)
        return nodes[1]
        