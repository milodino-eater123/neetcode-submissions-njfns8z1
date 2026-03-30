from collections import defaultdict
class Solution:
    def jump(self, nums: List[int]) -> int:
        #choosing the farthest range index is always the best, thus greedy
        #because gives more options

        l,r = 0,0
        steps = 0
        maxReach = 0
        while True:
            if r >= len(nums)-1:
                return steps
            #find new max reach
            for i in range(l,r+1):
                if i < len(nums):
                    maxReach = max(maxReach,i+nums[i])

            #jump to make reach bigger
            steps += 1
            l,r = r+1,maxReach




        
        