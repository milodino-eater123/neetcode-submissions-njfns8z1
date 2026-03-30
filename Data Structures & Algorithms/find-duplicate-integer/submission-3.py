class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #solution while modifying array nums
        
        #insight: each number corresponds to a
        #position in nums
        i = 0
        while True:
            if nums[i] < 0:
                return i
            temp = i 
            i = nums[i]
            nums[temp] *= -1 
        
        for i in range(0,len(nums)):
            nums[i] *= -1
        






        