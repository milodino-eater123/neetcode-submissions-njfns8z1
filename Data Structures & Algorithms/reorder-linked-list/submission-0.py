# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
     def reorderList(self, head: Optional[ListNode]) -> None:
        #slow and fast pointers traverse list
        #until fast at end, slow at midpoint
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #reverse 2nd half of linked list
        prev = None
        cur = slow.next
        slow.next = None

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        reverse = prev

        #construct res from first half and reversed 2nd half
        forward = head
        while forward and reverse:
                temp1, temp2 = forward.next,reverse.next
                forward.next = reverse
                reverse.next = temp1
                forward = temp1
                reverse = temp2
                

      
            




               