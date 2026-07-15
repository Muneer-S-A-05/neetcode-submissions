class Solution:
    def climbStairs(self, n: int) -> int:
        arr = [1,1,2,3]
        while len(arr)<=n:
            arr.append(arr[-1]+arr[-2])
        return arr[n]