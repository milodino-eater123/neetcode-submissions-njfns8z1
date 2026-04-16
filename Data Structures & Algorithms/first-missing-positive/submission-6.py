class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i]<=0:
                nums[i]=n+1
        
        for i in range(n):
            if abs(nums[i]) >= abs(n+1):
                continue
            num = abs(nums[i])-1
            if nums[num] > 0:
                nums[num] = -nums[num]
        
        for i,num in enumerate(nums):
            if num > 0:
                return i+1
        return n+1

