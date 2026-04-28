class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        
        for i,n in enumerate(nums):
            l,r=i+1,len(nums)-1
            while r>l:
                suhm = nums[l]+nums[r]
                if suhm > -n:
                    r -= 1
                elif suhm < -n:
                    l += 1
                else:
                    res.add((n,nums[l],nums[r]))
                    r -= 1
                    l += 1
        return list(res)

        