class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        maxSub = 0
        for x in nums:
            if maxSub<0:
                maxSub = 0
            maxSub += x
            res = max(res,maxSub)
        return res