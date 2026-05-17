class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        def find(i):
            if i in memo:
                return memo[i]


            length = 1
            
            for j in range(i+1,len(nums)):
                if nums[j] > nums[i]:
                    length = max(length,1 + find(j))
            
            memo[i] = length

            return length
        
        return max(find(x) for x in range(len(nums)))



        

        