class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        hset = set()
        if sum(nums) % 2 == 1:
            return False
        half = sum(nums)/2
        res = False
        def add(i,curSum):
            nonlocal res
            if (i,curSum) in hset:
                return
            if curSum == half:
                res = True
                return
            if curSum > half:
                return
            if i >= len(nums)-1:
                return
            
            hset.add((i,curSum))
            add(i+1,curSum+nums[i])
        
            add(i+1,curSum)
        
            
        


        add(0,0)
        return res
        