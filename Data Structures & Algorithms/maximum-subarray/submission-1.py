class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        maxSub = nums[0]
        for x in nums[1:]:
            if maxSub<0:
                maxSub = x
            else:
                maxSub+=x
            res = max(res,maxSub)
        return res