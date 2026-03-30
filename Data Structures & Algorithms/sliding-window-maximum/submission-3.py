from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        def push(lst,n):
            while lst and nums[n] >= nums[lst[-1]]:
                lst.pop()
            lst.append(n)

        mq = deque([])

        #1.Construct Window
        for i in range(0,k):
            push(mq,i)
        
        res.append(nums[mq[0]])

        #2.Slide Window
        l,r = 0,k-1
        while r + 1 < len(nums):
            #a)Shrink
            l += 1 

            #b)Expand, push to mdq.
            push(mq,r+1)
            r += 1 

            #get max
            while mq[0] < l:
                mq.popleft()
            
            res.append(nums[mq[0]])

        return res



        
 
       

        



            


        

        