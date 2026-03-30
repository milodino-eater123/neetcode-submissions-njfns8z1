class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        #sort the array first
        nums.sort()
        def kSum(target,start,k):
            k_res = set()
            if k == 2 :
                l,r = start, len(nums) - 1 
                while r > l:
                    two_sum = nums[l] + nums[r]
                    if two_sum == target:
                        k_res.add((nums[l],nums[r]))
                        l += 1 
                        r -= 1 
                    elif two_sum < target:
                        l += 1 
                    else:
                        r -= 1 
                return k_res
            for i in range(start,len(nums)):
                num = nums[i]
                for tupl in kSum(target-num,i+1,k-1):
                    tupl = (num,) + tupl
                    k_res.add(tupl)

            return k_res

        return [list(x) for x in kSum(target,0,4)]
        