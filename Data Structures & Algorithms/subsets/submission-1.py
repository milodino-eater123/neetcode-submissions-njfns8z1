class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def choose(i,path):
            nonlocal res
            if i >= len(nums):
                res.append(path[:])
                return
            #two choices
            path.append(nums[i])
            choose(i+1,path)
            
            path.pop()
            choose(i+1,path)

        choose(0,[])
        return res
        