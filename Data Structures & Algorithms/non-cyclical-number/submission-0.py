class Solution:
    def isHappy(self, n: int) -> bool:
        hset = set()
        while True:
            if n == 1:
                return True
            if n in hset:
                return False
            hset.add(n)
            temp = 0
            for digit in str(n):
                temp += int(digit)**2
            n = temp

            

        
        