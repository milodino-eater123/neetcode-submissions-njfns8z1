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
            return
        visited = set()
        hmap = defaultdict(lambda:Node())
        def clone(node):
            nonlocal visited, hmap
            if node in visited:
                return
            visited.add(node)
            hmap[node].val = node.val
            for child in node.neighbors:
                hmap[node].neighbors.append(hmap[child])
                clone(child)
        clone(node)
        return hmap[node]