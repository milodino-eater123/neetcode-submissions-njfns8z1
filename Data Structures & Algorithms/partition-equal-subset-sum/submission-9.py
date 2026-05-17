class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2==1:
            return False
        target = sum(nums)//2

        nums.sort()
        memo = set()
        def part(i,total):
            if total == target:
                return True
            if total > target:
                return False
            if i >= len(nums):
                return False
            if (i,total) in memo:
                return False
            
            memo.add((i,total))
            if total + nums[i] <= target:
                return part(i+1,total+nums[i]) or part(i+1,total)
            else:
                return False
        
        return part(0,0)

        