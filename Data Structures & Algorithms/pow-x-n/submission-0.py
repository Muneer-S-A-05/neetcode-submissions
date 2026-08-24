class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1
        res = 1
        absn = abs(n)
        fac = x

        while absn>0:
            if absn%2 == 1:
                res *= fac
            fac*=fac
            absn = absn//2
        
        return 1/res if n<0 else res