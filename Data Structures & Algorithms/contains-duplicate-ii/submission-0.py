class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hset = set()

        l,r = 0,0

        while r < len(nums):
            #if window has duplicate
            if nums[r] in hset:
                return True
            #if sliding window too big, shrink
            if r - l + 1 > k:
                hset.discard(nums[l])
                l += 1 
            #keeping record of all numbers in sw
            hset.add(nums[r])

            r += 1 

        return False
        