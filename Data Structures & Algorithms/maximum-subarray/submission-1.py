class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = 0
        maxSum = float('-inf')
        for n in nums:
            if curSum > 0:
                maxSum =max(maxSum,curSum+n)
                curSum += n
            else:
                maxSum = max(maxSum,n)
                curSum = n
        
        return maxSum
        