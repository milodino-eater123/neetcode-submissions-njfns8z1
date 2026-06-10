# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from heapq import heappush,heappop
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #initialise
        heap,dummy,i = [],ListNode(0),0
        cur=dummy
        for head in lists:
            if not head:
                continue
            heappush(heap,(head.val,i,head))
            i+=1
        #main
        while heap:
            val,_,node = heappop(heap)
            cur.next=node
            cur=cur.next
            if node.next:
                heappush(heap,(node.next.val,i,node.next))
                i+=1
        return dummy.next

        
        