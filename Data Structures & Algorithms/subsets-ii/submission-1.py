class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def subset(i,path):
            if i>=len(nums):
                res.append(path.copy())
                return
            
            path.append(nums[i])
            subset(i+1,path)
            path.pop()

            while i+1<len(nums) and nums[i]==nums[i+1]:
                i+=1 

            subset(i+1,path)

        subset(0,[])
        return res
        

            

        