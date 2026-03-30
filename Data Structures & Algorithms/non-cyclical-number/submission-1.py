class Solution:
    def isHappy(self, n: int) -> bool:
        def sumOfSquares(n):
            temp = 0
            for digit in str(n):
                temp += int(digit)**2
            return temp
        slow = n
        fast = sumOfSquares(n)
        while slow != fast:
            slow = sumOfSquares(slow)
            fast = sumOfSquares(sumOfSquares(fast))

        return True if slow == 1 else False

            

        
        