"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = Node(0)
        copy = dummy
        cur = head
        hmap = {None:None}
        while cur:
            copy.next = Node(cur.val)
            hmap[cur] = copy.next
            cur = cur.next
            copy = copy.next


        copy1 = dummy.next
        cur1 = head
        while cur1:
            copy1.random = hmap[cur1.random]
            copy1 = copy1.next
            cur1 = cur1.next
         
        return dummy.next
        