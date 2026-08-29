class Solution:
    def getSum(self, a: int, b: int) -> int:
        while b:
            a,b = (a^b) & 0xffffffff, ((a&b)<<1) & 0xffffffff
        return (a) if a<=0x7fffffff else ~(a^0xffffffff)