class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #solution while modifying array nums
        
        i = 0
        while True:
            if nums[i] == 0:
                return i
            temp = i 
            i = nums[i]
            nums[temp] = 0





        