# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return

        l,r = head,head
        count = -1

        while r:
            if count >= n:
                l = l.next
            r = r.next
            count += 1
            
        print(l.val)
        if count < n and l == head:
            return head.next
        l.next = l.next.next
        return head
        
            
        