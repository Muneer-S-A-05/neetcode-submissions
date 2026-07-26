class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        dp[len(nums)-1] = 1

        for i in range(len(nums)-1,-1,-1):
            for x in range(i+1,len(nums)):
                if nums[x]>nums[i]:
                    dp[i] = max(dp[i],1+dp[x])        
        return max(dp)