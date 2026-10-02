# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l,r = 1,n
        g = (n+1)//2
        result = guess(g)
        while result!=0 and l<=r:
            if result>0:
                l=g+1
            else:
                r=g-1
            g = (l+r)//2
            result = guess(g)
        return g