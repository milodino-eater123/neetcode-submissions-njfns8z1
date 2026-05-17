from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        dp.append(nums[0])

        for i in range(1,len(nums)):
            if nums[i] > dp[-1]:
                dp.append(nums[i])
            else:
                low,high = 0,len(dp)-1
                while high>low:
                    mid = (high+low)//2
                    if nums[i] <= dp[mid]:
                        high = mid
                    elif nums[i] > dp[mid]:
                        low = mid + 1 
                dp[low] = nums[i]
        
        return len(dp)



        

        