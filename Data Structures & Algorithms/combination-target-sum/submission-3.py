class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        def add(i,total,path):
            nonlocal res
            #base cases
            if total == target:
                res.append(path.copy())
                return
            if i >= len(nums):
                return


            if total + nums[i] > target:
                return
            #choose to include num
            path.append(nums[i])
            add(i,total+nums[i],path)
            path.pop()
            
            #choose to not include num - include next num
            add(i+1,total,path)

        add(0,0,[])
        return res


        
        