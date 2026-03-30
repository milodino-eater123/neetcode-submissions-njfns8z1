# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        start = dummy
        l,r = head,head
        
        while True:
            counter = 0
            while r:
                if counter == k:
                    break
                counter += 1 
                r = r.next

            if counter < k:
                break
 
            next = r 
            temp1 = l
            while l != r:
                temp = l.next
                l.next = next
                next = l
                l = temp
            
        
            start.next = next
            start=temp1


        return dummy.next
            


