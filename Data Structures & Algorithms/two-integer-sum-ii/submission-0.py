class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r = 0, len(numbers) - 1
        while r > l:
            pair = numbers[r] + numbers[l]
            if pair == target:
                return [l+1,r+1]
            elif pair > target:
                r -= 1 
            else:
                l += 1 
        