# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        overflow = 0
        dummy = ListNode(0)
        cur = dummy
        while l1 or l2 or overflow:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            val = val1 + val2 + overflow
            
            cur.next = ListNode(val % 10)
            overflow = val // 10 

            cur = cur.next
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2

        return dummy.next


            

        



        