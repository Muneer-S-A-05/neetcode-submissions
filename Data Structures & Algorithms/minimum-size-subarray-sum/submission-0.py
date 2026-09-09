class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = len(nums)+1
        cursum = 0
        i = 0
        for j in range(len(nums)):
            cursum += nums[j]
            while cursum>=target:
                res = min(res,j-i+1)
                cursum -= nums[i]
                i += 1
        return 0 if res>len(nums) else res