class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        def add(i,path,total):
            if i>=len(nums):
                return
            if total==target:
                res.append(path.copy())
                return
            if total+nums[i]>target:
                return
            
            path.append(nums[i])
            add(i,path,total+nums[i])
            path.pop()

            add(i+1,path,total)
        
        add(0,[],0)
        return res

    
        