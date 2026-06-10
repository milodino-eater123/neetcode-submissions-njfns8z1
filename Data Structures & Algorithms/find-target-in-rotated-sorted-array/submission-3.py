class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low,high = 0,len(nums)-1
        while high>=low:
            mid=(high+low)//2
            if nums[mid]==target:
                return mid
            elif (nums[mid]<nums[high] and nums[mid]<target<=nums[high])or(nums[mid]>nums[high] and (target>nums[mid] or target<=nums[high])):
                low = mid+1
            else:
                high = mid-1
        return -1



        