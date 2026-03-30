class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        #sort the list
        nums.sort()

        #iterate through list
        for i,target in enumerate(nums):
            l,r = i+1, len(nums) - 1 
            while r > l:
                two_sum = nums[l] + nums[r]
                if two_sum == -target:
                    res.add((target,nums[l],nums[r]))
                    l += 1 
                elif two_sum > -target:
                    r -= 1 
                else:
                    l += 1 


        return [list(x) for x in res]
        