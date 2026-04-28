class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r = 0,len(numbers)-1

        while numbers[l] + numbers[r] != target:
            suhm = numbers[l] + numbers[r]

            if suhm > target:
                r -= 1
            
            else:
                l += 1
        
        return [l+1,r+1]
 
