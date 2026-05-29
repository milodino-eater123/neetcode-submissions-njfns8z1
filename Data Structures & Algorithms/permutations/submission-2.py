class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def math(path,used):
            if len(path)==len(nums):
                res.append(path.copy())
            
            for n in nums:
                if n in used:
                    continue
                path.append(n)
                used.add(n)
                math(path,used)
                path.pop()
                used.remove(n)

        math([],set())
        return res

        