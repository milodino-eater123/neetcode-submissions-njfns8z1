class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #initialise
        low,high = 0, len(nums) - 1
        
        while high > low:
            mid = (high+low)//2
            #if left is sorted
            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid
                else:
                    low = mid + 1 
            #if right is sorted
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid
                else:
                    high = mid - 1 

            
        if nums[low] == target:
            return low
        else:
            return -1
        