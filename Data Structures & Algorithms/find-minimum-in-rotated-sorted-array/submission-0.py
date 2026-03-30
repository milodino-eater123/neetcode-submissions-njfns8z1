class Solution:
    def findMin(self, nums: List[int]) -> int:
        last = nums[-1]
        low,high = 0, len(nums) -1
        while high > low:
            mid = (low+high)//2
            if nums[mid] < last:
                high = mid
            elif nums[mid] > last:
                low = mid + 1 
        return nums[low]
