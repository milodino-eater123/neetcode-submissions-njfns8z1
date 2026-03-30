# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        count1 = 0
        cur1 = l1
        while cur1:
            count1 += 1 
            cur1 = cur1.next

        count2 = 0
        cur2 = l2
        while cur2:
            count2 += 1
            cur2 = cur2.next
        
        if count1 > count2:
            count2 = count1-count2
            count1 = 0
        else:
            count1 = count2 - count1
            count2 = 0

        #recursively buid

        
        
        def build(list1,list2,node,overflow):
            #base case
            if list1 and not list2:
                list2 = ListNode(0)
            elif list2 and not list1:
                list1 = ListNode(0)
                
            if not list1 and not list2:
                if overflow == 0:
                    return
                else:
                    node.next = ListNode(overflow)
                    return

            
            #real calculations
            suhm = list1.val + list2.val + overflow 
            node.next = ListNode(suhm % 10)

            #func call
            build(list1.next,list2.next,node.next,suhm//10)
        

        dummy = ListNode(0)
        build(l1,l2,dummy,0)

        return dummy.next
        



        