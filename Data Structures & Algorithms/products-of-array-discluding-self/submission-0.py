class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        fromLeft,fromRight = [1],[1]
        for n in nums:
            fromLeft.append(fromLeft[-1]*n)

        for n in nums[::-1]:
            fromRight.append(fromRight[-1]*n)
        fromRight = fromRight[::-1]
        
        output = []
        for i in range(len(nums)):
            output.append(fromLeft[i]*fromRight[i+1])

        return output

        