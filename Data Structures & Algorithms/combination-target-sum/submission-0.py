class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def add(i,total,path):
            nonlocal res
            if total > target:
                return
            elif total == target:
                res.append(path[:])
                return
            
            for j in range(i,len(nums)):
                n = nums[j]
                path.append(n)
                add(j,total+n,path)
                path.pop()

        add(0,0,[])
        return res
        