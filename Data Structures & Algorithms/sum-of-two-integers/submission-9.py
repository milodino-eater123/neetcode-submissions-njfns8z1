class Solution:
    def getSum(self, a: int, b: int) -> int:
        suhm = (a^b) & 0xFFFFFFFF
        carry = (a&b) << 1 & 0xFFFFFFFF
        while carry > 0:
            temp = suhm
            suhm = (suhm^carry) & 0xFFFFFFFF
            carry= ((temp&carry)<<1) 
        
        if suhm > 0x7FFFFFFF:
            suhm = ~(suhm^0xFFFFFFFF)
        return suhm 


        
        







        
        
        