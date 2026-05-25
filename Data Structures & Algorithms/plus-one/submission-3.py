class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits)-1,-1,-1):
            d = digits[i]
            total = d+carry
            digit = total%10
            carry = total//10
            digits[i]=digit
            if not carry:
                break
        if carry:
            digits = [1]+digits
        return digits

        