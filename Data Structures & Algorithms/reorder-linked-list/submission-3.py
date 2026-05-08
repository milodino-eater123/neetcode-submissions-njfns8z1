# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow,fast = head,head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        cur = slow.next
        slow.next = None

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        tail = prev
        cur = ListNode(0)
        

        while head and tail:
            cur.next = head
            head = head.next
            cur.next.next = tail
            tail = tail.next
            cur = cur.next.next
            
            
        
        cur.next = head if head else None

        
        
        
        


        