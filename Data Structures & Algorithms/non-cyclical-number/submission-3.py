class Solution:
    def isHappy(self, n: int) -> bool:
        def happy(num):
            res = 0
            for c in str(num):
                n = int(c)
                res += (n**2)
            return res
            
        slow,fast = n,happy(n)

        while slow != fast:
            slow = happy(slow)
            fast = happy(happy(fast))
            
        return slow==1

        