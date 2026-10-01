class Solution:
    def mySqrt(self, x: int) -> int:
        i = 1
        while x>=i*i:
            i+=1
        return i-1