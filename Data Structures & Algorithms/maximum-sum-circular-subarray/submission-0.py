class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        gmax = nums[0]
        cmax = 0
        gmin = nums[0]
        cmin = 0
        s = 0
        for x in nums:
            cmax = max(cmax+x,x)
            gmax = max(gmax,cmax)
            cmin = min(cmin+x,x)
            gmin = min(gmin,cmin)
            s += x
        return max(gmax,s-gmin) if gmax>0 else gmax