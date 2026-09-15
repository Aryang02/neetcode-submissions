class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        while b != 0:
            c = (a & b) << 1;
            a = (a ^ b) & MASK
            b = c & MASK
        
        if a > 0x7FFFFFFF:
            a = ~(a^MASK)
        return a