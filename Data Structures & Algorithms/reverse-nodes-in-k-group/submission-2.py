# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        cur,count = head,0
        front = dummy
        
        while cur:
            count += 1
            cur=cur.next
            if count == k:
                back = cur
                prev,node = back,front.next
                temp1 = front.next
                while node != back:
                    temp = node.next
                    node.next = prev
                    prev = node
                    node = temp
                front.next = prev
                front = temp1
                count = 0
            
        return dummy.next

        