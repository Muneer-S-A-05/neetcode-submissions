class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return True

        lastTrue = len(nums)-1
        
        for i in range(len(nums)-2,-1,-1):
            if nums[i]+i >= len(nums) or lastTrue<=i+nums[i]:
                lastTrue = i
        
        return lastTrue == 0