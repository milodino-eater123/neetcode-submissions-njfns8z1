class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        def suhm(path,i,total):
            nonlocal res
            if total == target:
                res.append(path.copy())
                return
            if total > target or i>=len(nums):
                return


            suhm(path,i+1,total)


            path.append(nums[i])

            if total + nums[i] <= target:
                suhm(path,i,total+nums[i])
            path.pop()


        

        suhm([],0,0)
        return res


        
        