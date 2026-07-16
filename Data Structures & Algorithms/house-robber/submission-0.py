class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        nums.append(0)
        for i in range(n-3,-1,-1):
            nums[i] += max(nums[i+2],nums[i+3])
        print(nums)
        return max(nums[0],nums[1])