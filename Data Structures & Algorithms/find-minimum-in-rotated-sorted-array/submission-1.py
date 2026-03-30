class Solution:
    def findMin(self, nums: List[int]) -> int:
        last = nums[-1]
        low,high = 0, len(nums) -1
        while high > low:
            mid = (low+high)//2
            if nums[mid] < nums[high]:
                high = mid
            elif nums[mid] > nums[high]:
                low = mid + 1 
        return nums[low]


        #if mid is less than last, mid to last is sorted,
        #min is mid or below mid, thus in range low-mid

        #if mid is more than last, mid to last has pivot point,
        #min is thus in range mid+1 to high
