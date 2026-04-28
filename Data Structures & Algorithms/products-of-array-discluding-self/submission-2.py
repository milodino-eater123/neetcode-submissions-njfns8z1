class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        fromLeft = [1]

        for n in nums:
            new = fromLeft[-1] * n
            fromLeft.append(new)

        fromRight = [1]

        for n in nums[::-1]:
            new = fromRight[-1] * n
            fromRight.append(new)

        res = []

        for i in range(len(nums)):
            res.append(fromLeft[i]*fromRight[-2-i])

        return res

        

        
        


        
        