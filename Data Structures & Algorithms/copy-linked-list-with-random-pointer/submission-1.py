"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
from collections import defaultdict
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hmap = defaultdict(lambda: Node(0))
        hmap[None] = None

        
        cur = head
        while cur:
            hmap[cur].val = cur.val
            hmap[cur].next = hmap[cur.next]
            hmap[cur].random = hmap[cur.random]
            cur = cur.next

        return hmap[head]

        