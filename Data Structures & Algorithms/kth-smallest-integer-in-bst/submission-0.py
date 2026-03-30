# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from heapq import heappush,heappop,heapify
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        maxHeap = []
        def search(node):
            nonlocal maxHeap
            if not node:
                return
            
            heappush(maxHeap,-node.val)
            if len(maxHeap) > k:
                heappop(maxHeap)

            search(node.left)
            search(node.right)
        
        search(root)
        return -maxHeap[0]



        