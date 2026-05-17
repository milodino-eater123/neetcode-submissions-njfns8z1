class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2==1:
            return False
        target = sum(nums)//2

        def part(i,total):
            if total == target:
                return True
            if total > target:
                return False
            if i >= len(nums):
                return False
            
            return part(i+1,total+nums[i]) or part(i+1,total)
        
        return part(0,0)

        