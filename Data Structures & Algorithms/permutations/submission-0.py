class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def build(options,path):
            nonlocal res
            if not options:
                res.append(path[:])
                return

            for i,n in enumerate(options):
                path.append(n)
                build(options[:i]+options[i+1:],path)
                path.pop()

        build(nums,[])
        return res
        
        
        