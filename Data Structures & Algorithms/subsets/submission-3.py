class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def build(path,i):
            nonlocal res
            if i >= len(nums):
                res.append(path.copy())
                return
            
            build(path,i+1)

            path.append(nums[i])

            build(path,i+1)

            path.pop()
            
        

        build([],0)
        return res
        





        