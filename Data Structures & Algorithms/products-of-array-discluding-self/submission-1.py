class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1,2,4,6]
        # [1,1,2,8]
        # [48,24,12,8]
        output = [1]
        for i in range(1,len(nums)):
            #previous number's sum x number to immediate left
            output.append(output[-1]*nums[i-1])
        
        temp = 1 
        for i in range(len(nums)-2,-1,-1):
            temp *= nums[i+1]
            output[i] *= temp

        return output


        
        


        
        