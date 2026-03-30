class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def choose(i,path):
            nonlocal res
            if i >= len(nums):
                res.append(path)
                return
            #two choices
            choose(i+1,path)

            choose(i+1,path+[nums[i]])

        choose(0,[])
        return res
        