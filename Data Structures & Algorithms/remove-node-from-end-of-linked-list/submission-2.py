# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #two pointers, traverse down, 0, 0+n
        first,second = head,head
        counter = 0 
        while second:
            second = second.next 
            if counter >= n+1:
                first = first.next
            counter += 1
    
        #edge case
        if counter == n:
            return head.next
        #perform deletion of node
        first.next = first.next.next

        return head