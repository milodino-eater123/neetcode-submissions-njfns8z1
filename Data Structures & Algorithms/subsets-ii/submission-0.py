class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def build(i,path):
            nonlocal res
            if i >= len(nums):
                res.append(path.copy())
                return

            n = nums[i]
            path.append(n)
            build(i+1,path)
            path.pop()


            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1 
            build(i+1,path)
        
        build(0,[])
        return res


            

        